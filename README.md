
# Teste Elo7 - SRE / DevOps

Realização do cenário proposto através de IaaC e uma entrega conteinerizada.  

## Tecnologias utilizadas

**Infraestrutura:** Vagrant, VirtualBox

**Conteiner:** Docker

**Orquestração:** Kubernetes - Minikube

**Aplicação:** Python - Flask




## Instalando Componentes

- [Vagrant](https://linuxize.com/post/how-to-install-vagrant-on-ubuntu-18-04/) 
- [Insomnia](https://insomnia.rest/download) 


## Iniciando a VM
Clone o repositório 
```bash
  git clone https://github.com/bagrielll/eloteste.git
```
Crie um diretório para os scripts do Kubernetes
```bash
  mkdir /home/$USER/eloteste/vagrant/scripts/
```
Entre no diretório /vagrant/ e inicie a VM

```bash
  cd /eloteste/vagrant/ && vagrant up
```
Acesse a VM

```bash
  vagrant ssh

```
## Iniciando a aplicação
Inicie o Minikube

```bash
  minikube start
```
Crie um namespace

```bash
  kubectl create namespace eloteste
```
Acesse o diretório /scripts/ para criar o Deployment e o Service
```bash
  cd /scripts/ 
  kubectl apply -f deployments.yaml -n eloteste
  kubectl apply -f services.yaml -n eloteste
```

Verifique se está tudo UP e copie o nome do POD
```bash
  kubectl get all -n eloteste
```

Cole o nome do POD e execute o Port-Forward
```bash
  kubectl port-forward --address 0.0.0.0 <POD> 3000:3000 -n eloteste & 
```

## Utilizando a aplicação através do Insomnia
Crie uma nova requisição
```bash
Método: POST
URL: http://127.0.0.1:3000/ 
```

Selecione o Body: text-json
```JSON
{
    "maxCords": "5 5",
    "sondas": [{
        "cordsSonda": "1 2 N",
        "comandos": "LMLMLMLMM"
    },{
        "cordsSonda": "3 3 E",
        "comandos": "MMRMMRMRRM"
    }]
}
```
Cole e aguarde a saída.

