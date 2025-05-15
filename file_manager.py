import os, shlex
HOME = os.getcwd()

def run(cmd, args):
    try:
        match cmd:
            case "touch": open(args[0], "w").write(args[1] if len(args) > 1 else "")
            case "cat": print(open(args[0]).read())
            case "rm": os.remove(args[0])
            case "mkdir": os.mkdir(args[0])
            case "cd": os.chdir(args[0]); print(f"[+] {os.getcwd()}")
            case "ls": print("📂", *[" - "+f for f in os.listdir()], sep="\n" if os.listdir() else "\n(empty)")
            case "home": os.chdir(HOME)
            case "help": print("""touch <f> [txt], cat <f>, rm <f>, mkdir <d>, cd <d>, ls, home, help, exit""")
            case _: print("[!] Unknown command")
    except Exception as e:
        print(f"[!] Error: {e}")

print("📁 Python CLI File Manager (type 'help')\n")
while True:
    try:
        parts = shlex.split(input(f"{os.getcwd()}$ "))
        if not parts: continue
        if parts[0] == "exit": break
        run(parts[0], parts[1:])
    except KeyboardInterrupt:
        print("\n👋 Exiting."); break
