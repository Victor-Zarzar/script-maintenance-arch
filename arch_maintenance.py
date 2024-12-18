import os
import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar: {command}\n{e}")

def update_system():
    print("🔄 Atualizando pacotes do sistema...")
    run_command("sudo pacman -Syu --noconfirm")

def remove_orphans():
    print("🧹 Removendo pacotes órfãos...")
    try:
        orphans = subprocess.check_output("pacman -Qtdq", shell=True, text=True).split()
        if orphans:
            run_command(f"sudo pacman -Rns {' '.join(orphans)} --noconfirm")
        else:
            print("Nenhum pacote órfão encontrado.")
    except subprocess.CalledProcessError:
        print("Nenhum pacote órfão encontrado.")

def clean_pacman_cache():
    print("🗂 Limpando cache do Pacman...")
    run_command("sudo pacman -Sc --noconfirm")

def clean_docker():
    print("🐳 Limpando imagens, containers e volumes não usados do Docker...")
    run_command("docker system prune -af --volumes")

def clean_logs():
    print("🗂 Limpando logs antigos...")
    run_command("sudo journalctl --vacuum-time=7d")

def clean_user_caches():
    print("🧹 Limpando caches gerais...")
    os.system("rm -rf ~/.cache/*")
    os.system("sudo rm -rf /var/cache/*")

if __name__ == "__main__":
    update_system()
    remove_orphans()
    clean_pacman_cache()
    clean_docker()
    clean_logs()
    clean_user_caches()
    print("✅ Manutenção do Arch Linux concluída!")
