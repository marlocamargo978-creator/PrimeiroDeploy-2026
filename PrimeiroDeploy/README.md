# Primeiro Deploy remoto (2026)

Este projeto documenta o processo de configuração de um ambiente de desenvolvimento remoto e o deploy de uma aplicaçao web Flask em um servidor Linux local.

## Objetivo
Transformar um notebook antigo em um servidor Linux Headless e desenvolver a partir de outra maquina usando o VS Code remoto SSH.

## Arquitetura
* **Cliente (PC1):** Máquina de desenvolvimento (Onde o código foi escrito)
* **Servidor (PC2):** Linux mint Debian edition(LMDE 7) rodando a aplicação.
* **Conexão:** SSH via rede local (LAN).

## Passo a passo do processo

### 1. Reconhecimento de rede
Utilizei o 'nmap' para encontrar o ip do servidor na rede local e identificar portas abertas.

```bash
# Scan para descobrir dispositivos na rede

sudo nmap -sn <ip_do_servidor>

# Scan detalhado no alvo para confirmar serviço SSH (porta 22)

sudo nmap -sV -O <ip_do_servidor>
```
### 2. Conexão e configuração SSH
Estabeleci uma conexão segura com o servidor sem necessidade de senha a cada login (SSH Keys).

```bash
#gerando o par de chaves no cliente

ssh-keygen -t rsa -b 4096

#Enviando a chave publica para o servidor

ssh-copy-id usuario@<ip_do_servidor>

#Acesso via terminal
ssh usuario@<ip_do_servidor>
```
### 3. Ambiente de desenvolvimento (VS Code)
* **Instalação da extensão Remote-SSH no VS Code.**
* **Configuração do host no arquivo** `~/.ssh/config`**.**
* **Acesso remoto aos arquivos do servidor diretamente pelo editor do cliente.**

### 4. Estrutura do projeto

```text
/PrimeiroDeploy
    |-- meu_site.py        # Lógica do servidor (Flask)
    |-- /templates
          |-- index.html   # Front-end (HTML/CSS)
```
### 5. Execução (Deploy)
Comando para rodar a aplicação em modo de desenvolvimento (acessivel por qualquer dispositivo na rede local):

```Python
# No arquivo meu_site.py
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```
Executando no terminal do servidor:
```bash
python3 meu_site.py
```
# Resultado

Acesso via navegador no cliente: `http://<ip_do_servidor:5000>`

## Status: Funcionando(01/01/2026).


