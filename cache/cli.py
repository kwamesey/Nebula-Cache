import argparse, shlex
from .cluster import CacheCluster
from .utils import print_nodes_table, info, warn, error

def repl(cluster: CacheCluster):
    info("NebulaCache interactive mode. Type 'help' for commands.")
    while True:
        try:
            raw = input('> ').strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not raw:
            continue
        parts = shlex.split(raw)
        cmd = parts[0].lower()
        if cmd in ('exit', 'quit'):
            info('bye 👋')
            break
        elif cmd == 'help':
            print('''Commands:\n  put <key> <value>\n  get <key>\n  add-node\n  remove-node <id>\n  fail-node <id>\n  heal-node <id>\n  show-nodes\n  where <key>\n  exit''')
        elif cmd == 'put' and len(parts) >= 3:
            key = parts[1]
            value = ' '.join(parts[2:])
            cluster.put(key, value)
            info(f"stored {key} → {value}")
        elif cmd == 'get' and len(parts) == 2:
            key = parts[1]
            val = cluster.get(key)
            if val is not None:
                info(f"{key} = {val}")
            else:
                warn('not found (or replicas down)')
        elif cmd == 'add-node':
            new_id = f"node-{len(cluster.nodes)+1}"
            cluster.add_node(new_id)
            info(f"added {new_id}")
        elif cmd == 'remove-node' and len(parts) == 2:
            cluster.remove_node(parts[1])
            warn(f"removed {parts[1]}")
        elif cmd == 'fail-node' and len(parts) == 2:
            cluster.fail_node(parts[1])
            warn(f"{parts[1]} marked DOWN")
        elif cmd == 'heal-node' and len(parts) == 2:
            cluster.heal_node(parts[1])
            info(f"{parts[1]} healed")
        elif cmd == 'show-nodes':
            print_nodes_table(cluster.list_nodes())
        elif cmd == 'where' and len(parts) == 2:
            owners = cluster.key_owners(parts[1])
            info(f"{parts[1]} → {', '.join(owners)}")
        else:
            error('unknown command')

def main():
    parser = argparse.ArgumentParser(description='NebulaCache - distributed cache simulator')
    parser.add_argument('--nodes', type=int, default=3)
    parser.add_argument('--replication', type=int, default=2)
    args = parser.parse_args()
    cluster = CacheCluster(replication_factor=args.replication)
    for i in range(args.nodes):
        cluster.add_node(f'node-{i+1}')
    print_nodes_table(cluster.list_nodes())
    repl(cluster)

if __name__ == '__main__':
    main()
