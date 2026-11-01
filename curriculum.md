# Currículo — Engenharia de sistemas ICC ferroviários

**Objetivo:** projetar, documentar e validar uma arquitetura ICC ponta a ponta, cobrindo os requisitos técnicos do perfil ICC System Designer, com evidência prática.

**Ritmo:** 3 sessões de 90 minutos por semana (4,5 h). São 43 temas. Com cerca de 3 sessões por tema, a formação leva de 10 a 12 meses. Não há prazo fixo.

**Abordagem:** `theory_first`. Todo tema começa do zero neste estudo, com aula completa: o problema, como funciona, vocabulário em português e inglês, exemplos, erros comuns e checagens. A prática vem depois. Experiência profissional e estudos em outros programas não encurtam a teoria nem contam como evidência.

## Projeto progressivo: ICC Linha Aurora

Em `projects/icc-linha-aurora/`, cada fase acrescenta uma parte ao centro de controle de uma linha fictícia, do requisito ao dossiê final. Todos os dados são inventados.

## Critério de conclusão (vale para todos os itens)

Um item só é fechado com **domínio 80**, com os IDs das evidências registrados no `session-log.md`:

1. **Feynman:** explicar o tema com as próprias palavras, sem ajuda.
2. **Aplicação padrão:** fazer de ponta a ponta o resultado observável do item, sem ajuda.
3. **Transferência:** fazer o mesmo num contexto novo, sem ajuda.

Texto do tutor, cards, diagramas gerados e outras mídias nunca contam como evidência.

## Inglês

Cada lição traz glossário técnico PT/EN, e cada fase termina com uma explicação curta do tema em inglês. O inglês geral é estudado em uma formação própria.

## Laboratório

As máquinas virtuais ficam em `E:`, fora do Google Drive. Licença, versão e disponibilidade de cada produto são verificadas na lição correspondente. Quando um produto não puder ser instalado, a lição usa um substituto e registra isso de forma explícita.

## Roteiro

### Fase 0 — Visão de sistema

**Entrega da fase:** Diagrama de contexto da Linha Aurora.

- [ ] **0.1 O que é um ICC: ATS, SCADA e segurança** (`lesson_01_icc_visao` / `topic_icc_visao`)
  - *Resultado observável:* Desenhar o contexto de um ICC, dizer qual subsistema trata cada função e separar o que é vital do que não é.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Aplicar o mesmo raciocínio a um bonde ou a uma linha principal.
- [ ] **0.2 Engenharia de sistemas e ciclo em V** (`lesson_02_eng_sistemas` / `topic_eng_sistemas`)
  - *Resultado observável:* Colocar as etapas de um projeto no ciclo em V e ligar cada etapa de definição à verificação que a confere.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Mapear o ciclo em V de uma troca de sistema já em operação.
  - *Revisita:* O que é um ICC: ATS, SCADA e segurança (`topic_icc_visao`).

**Fechamento da fase:** explicação de 2 minutos em inglês sobre a entrega da fase.

### Fase 1 — Sinalização moderna

**Entrega da fase:** Conceito de operação da Linha Aurora.

- [ ] **1.1 Intertravamento eletrônico e lógica vital** (`lesson_03_intertravamento` / `topic_intertravamento_eletronico`)
  - *Resultado observável:* Explicar rota, travamento e aspecto, comparar relé e computador e justificar como o processamento redundante mantém o estado seguro.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Analisar uma tabela de controle de um pátio novo.
  - *Revisita:* O que é um ICC: ATS, SCADA e segurança (`topic_icc_visao`).
- [ ] **1.2 ATS: supervisão automática dos trens** (`lesson_04_ats` / `topic_ats`)
  - *Resultado observável:* Descrever rastreamento, roteamento automático, regulação e tabela horária, e prever o que o ATS faz numa perturbação.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Planejar a resposta a uma perturbação em bifurcação.
  - *Revisita:* Intertravamento eletrônico e lógica vital (`topic_intertravamento_eletronico`).
- [ ] **1.3 ATP, ATO, CBTC e ETCS** (`lesson_05_atc_cbtc` / `topic_atc_cbtc_etcs`)
  - *Resultado observável:* Comparar bloco fixo e bloco móvel e posicionar ATP, ATO e ATS numa arquitetura CBTC e numa ETCS.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Avaliar a migração de uma linha convencional para CBTC.
  - *Revisita:* ATS: supervisão automática dos trens (`topic_ats`).

**Fechamento da fase:** explicação de 2 minutos em inglês sobre a entrega da fase.

### Fase 2 — Redes

**Entrega da fase:** Plano de rede da Linha Aurora.

- [ ] **2.1 TCP/IP avançado** (`lesson_06_tcpip` / `topic_tcpip`)
  - *Resultado observável:* Calcular sub-redes, explicar ARP, TCP, UDP e portas e ler uma captura de pacotes.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Endereçar uma rede com outro número de estações.
- [ ] **2.2 VLAN e roteamento básico** (`lesson_07_vlan_roteamento` / `topic_vlan_roteamento`)
  - *Resultado observável:* Segmentar a rede em VLANs e definir rotas para que só os fluxos necessários se comuniquem.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Segmentar a rede de um pátio.
  - *Revisita:* TCP/IP avançado (`topic_tcpip`).
- [ ] **2.3 Firewall e VPN** (`lesson_08_firewall_vpn` / `topic_firewall_vpn`)
  - *Resultado observável:* Escrever regras de firewall por fluxo e desenhar um acesso remoto de manutenção com VPN.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Rever as regras para um fornecedor novo.
  - *Revisita:* VLAN e roteamento básico (`topic_vlan_roteamento`).
- [ ] **2.4 Troubleshooting de conectividade** (`lesson_09_troubleshooting` / `topic_troubleshooting_rede`)
  - *Resultado observável:* Seguir um método por camadas para achar a causa de uma falha de comunicação entre dois servidores.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Diagnosticar um defeito novo sem roteiro.
  - *Revisita:* TCP/IP avançado (`topic_tcpip`).

**Fechamento da fase:** explicação de 2 minutos em inglês sobre a entrega da fase.

### Fase 3 — Controle e comunicação

**Entrega da fase:** Bancada PLC + SCADA da Linha Aurora.

- [ ] **3.1 PLC e IEC 61131-3** (`lesson_10_plc` / `topic_plc`)
  - *Resultado observável:* Explicar o ciclo de varredura e escrever uma lógica simples de controle de equipamento fixo em ladder.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Adaptar a lógica a outro equipamento.
- [ ] **3.2 SCADA: tags, alarmes e histórico** (`lesson_11_scada` / `topic_scada`)
  - *Resultado observável:* Montar uma tela com tags, comandos, alarmes e histórico ligada a um PLC simulado.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Criar a tela de outro sistema de estação.
  - *Revisita:* PLC e IEC 61131-3 (`topic_plc`).
- [ ] **3.3 Modbus, DNP3, IEC 60870-5-104 e OPC UA** (`lesson_12_protocolos` / `topic_protocolos`)
  - *Resultado observável:* Comparar os protocolos, escolher um para cada interface e interpretar tráfego real capturado na bancada.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Justificar o protocolo de uma interface nova.
  - *Revisita:* TCP/IP avançado (`topic_tcpip`).
- [ ] **3.4 Comunicação segura ferroviária (EN 50159)** (`lesson_13_comunicacao_segura` / `topic_comunicacao_segura`)
  - *Resultado observável:* Listar as ameaças à mensagem e as defesas de uma comunicação ligada à segurança.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Analisar um enlace por rádio.
  - *Revisita:* Modbus, DNP3, IEC 60870-5-104 e OPC UA (`topic_protocolos`).

**Fechamento da fase:** explicação de 2 minutos em inglês sobre a entrega da fase.

### Fase 4 — Requisitos e modelagem

**Entrega da fase:** Modelo de sistema da Linha Aurora.

- [ ] **4.1 Requisitos e rastreabilidade** (`lesson_14_requisitos` / `topic_requisitos`)
  - *Resultado observável:* Transformar uma necessidade operacional em requisitos verificáveis e manter a matriz de rastreabilidade.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Reescrever uma especificação ruim de outro subsistema.
  - *Revisita:* Engenharia de sistemas e ciclo em V (`topic_eng_sistemas`).
- [ ] **4.2 UML: casos de uso, classes, sequência e estados** (`lesson_15_uml` / `topic_uml`)
  - *Resultado observável:* Modelar uma função do ICC com os diagramas certos para cada pergunta de projeto.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Modelar uma função diferente sem exemplo.
  - *Revisita:* Requisitos e rastreabilidade (`topic_requisitos`).
- [ ] **4.3 SysML: blocos, requisitos e paramétricos** (`lesson_16_sysml` / `topic_sysml`)
  - *Resultado observável:* Construir um modelo SysML do ICC ligando requisitos, estrutura e comportamento.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Estender o modelo com um subsistema novo.
  - *Revisita:* UML: casos de uso, classes, sequência e estados (`topic_uml`).
- [ ] **4.4 Interfaces e fluxos de dados (ICD)** (`lesson_17_interfaces` / `topic_interfaces`)
  - *Resultado observável:* Escrever um documento de controle de interface com mensagens, tempos, erros e responsáveis.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Especificar a interface com um fornecedor externo.
  - *Revisita:* Modbus, DNP3, IEC 60870-5-104 e OPC UA (`topic_protocolos`).
- [ ] **4.5 Projeto baseado em modelos e simulação** (`lesson_18_simulacao` / `topic_simulacao`)
  - *Resultado observável:* Construir em Python uma simulação simples que compare duas opções de projeto com dados.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Usar a simulação para decidir uma questão nova de capacidade.
  - *Revisita:* SysML: blocos, requisitos e paramétricos (`topic_sysml`).

**Fechamento da fase:** explicação de 2 minutos em inglês sobre a entrega da fase.

### Fase 5 — Segurança e qualidade

**Entrega da fase:** Plano de V&V e análise de perigos da Linha Aurora.

- [ ] **5.1 RAMS e EN 50126** (`lesson_19_rams` / `topic_rams`)
  - *Resultado observável:* Calcular disponibilidade a partir de MTBF e MTTR e situar as atividades RAMS no ciclo de vida.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Comparar duas arquiteturas redundantes pelos números.
  - *Revisita:* Engenharia de sistemas e ciclo em V (`topic_eng_sistemas`).
- [ ] **5.2 SIL e análise de perigos** (`lesson_20_sil_perigos` / `topic_sil_perigos`)
  - *Resultado observável:* Conduzir uma análise de perigos, uma FMEA e uma árvore de falhas de uma função do ICC.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Analisar uma função nova.
  - *Revisita:* RAMS e EN 50126 (`topic_rams`).
- [ ] **5.3 Software ferroviário: da EN 50128 à EN 50716** (`lesson_21_en50716` / `topic_en50716`)
  - *Resultado observável:* Explicar o que a norma pede por nível de integridade, quais papéis existem e o que mudou com a EN 50716.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Planejar o processo de software de um módulo com outro nível.
  - *Revisita:* SIL e análise de perigos (`topic_sil_perigos`).
- [ ] **5.4 Caso de segurança (EN 50129)** (`lesson_22_caso_seguranca` / `topic_caso_seguranca`)
  - *Resultado observável:* Estruturar o argumento de um caso de segurança e ligar afirmações às evidências.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Avaliar um caso de segurança de terceiros.
  - *Revisita:* SIL e análise de perigos (`topic_sil_perigos`).
- [ ] **5.5 Verificação e validação** (`lesson_23_vv` / `topic_vv`)
  - *Resultado observável:* Escrever um plano de V&V com casos de teste rastreados aos requisitos, incluindo FAT e SAT.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Planejar a V&V de uma alteração em sistema em operação.
  - *Revisita:* Requisitos e rastreabilidade (`topic_requisitos`).
- [ ] **5.6 Cibersegurança ferroviária (IEC 62443)** (`lesson_24_ciberseguranca` / `topic_ciberseguranca`)
  - *Resultado observável:* Dividir o ICC em zonas e condutos e definir controles para cada um.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Avaliar o risco de uma conexão nova.
  - *Revisita:* Firewall e VPN (`topic_firewall_vpn`).

**Fechamento da fase:** explicação de 2 minutos em inglês sobre a entrega da fase.

### Fase 6 — Servidores e sistemas operacionais

**Entrega da fase:** Servidores do laboratório da Linha Aurora.

- [ ] **6.1 Servidores Dell, HPE e Lenovo** (`lesson_25_servidores` / `topic_servidores`)
  - *Resultado observável:* Dimensionar um servidor para uma carga e usar o conceito de gerenciamento remoto dos três fabricantes.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Refazer a escolha para outro fabricante.
- [ ] **6.2 Firmware e BIOS** (`lesson_26_firmware_bios` / `topic_firmware_bios`)
  - *Resultado observável:* Planejar a atualização de firmware de um servidor em operação, com teste e retorno.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Adaptar o plano a um cluster inteiro.
  - *Revisita:* Servidores Dell, HPE e Lenovo (`topic_servidores`).
- [ ] **6.3 Administração Linux** (`lesson_27_linux` / `topic_linux`)
  - *Resultado observável:* Instalar um Linux compatível com Red Hat, gerenciar usuários, pacotes, permissões e discos.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Repetir as tarefas essenciais em Oracle Linux.
- [ ] **6.4 Administração de Windows Server** (`lesson_28_windows_server` / `topic_windows_server`)
  - *Resultado observável:* Instalar um Windows Server, criar papéis e gerenciar usuários e atualizações.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Adaptar a configuração a um papel novo.
- [ ] **6.5 Serviços e logs** (`lesson_29_servicos_logs` / `topic_servicos_logs`)
  - *Resultado observável:* Diagnosticar um serviço parado pelos logs, no Linux e no Windows.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Diagnosticar outro serviço no sistema operacional oposto.
  - *Revisita:* Administração Linux (`topic_linux`).

**Fechamento da fase:** explicação de 2 minutos em inglês sobre a entrega da fase.

### Fase 7 — Virtualização e armazenamento

**Entrega da fase:** Cluster e armazenamento do laboratório.

- [ ] **7.1 Virtualização com Hyper-V** (`lesson_30_hyperv` / `topic_hyperv`)
  - *Resultado observável:* Criar e operar máquinas virtuais, redes e snapshots no Hyper-V do laboratório.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Recriar o ambiente a partir da documentação.
  - *Revisita:* Servidores Dell, HPE e Lenovo (`topic_servidores`).
- [ ] **7.2 VMware vSphere** (`lesson_31_vsphere` / `topic_vsphere`)
  - *Resultado observável:* Explicar ESXi, vCenter, vMotion e DRS e comparar com o Hyper-V para decidir uma implantação.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Migrar um desenho do Hyper-V para vSphere.
  - *Revisita:* Virtualização com Hyper-V (`topic_hyperv`).
- [ ] **7.3 Cluster e alta disponibilidade** (`lesson_32_cluster` / `topic_cluster`)
  - *Resultado observável:* Configurar um cluster de teste, calcular reserva de capacidade e provar o failover.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Planejar uma manutenção sem parar o serviço.
  - *Revisita:* Virtualização com Hyper-V (`topic_hyperv`).
- [ ] **7.4 RAID** (`lesson_33_raid` / `topic_raid`)
  - *Resultado observável:* Escolher um nível de RAID por caso, montar um em VM e recuperar uma falha de disco.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Decidir para outra carga de trabalho.
  - *Revisita:* Administração Linux (`topic_linux`).
- [ ] **7.5 SAN, NAS e multipath** (`lesson_34_san_nas` / `topic_san_nas_multipath`)
  - *Resultado observável:* Comparar SAN e NAS, expor um volume por iSCSI e configurar multipath com teste de falha.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Escolher armazenamento para outro serviço.
  - *Revisita:* RAID (`topic_raid`).
- [ ] **7.6 Replicação** (`lesson_35_replicacao` / `topic_replicacao`)
  - *Resultado observável:* Comparar replicação síncrona e assíncrona e medir seu efeito em laboratório.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Definir a replicação entre dois centros.
  - *Revisita:* SAN, NAS e multipath (`topic_san_nas_multipath`).

**Fechamento da fase:** explicação de 2 minutos em inglês sobre a entrega da fase.

### Fase 8 — Operação

**Entrega da fase:** Backup, painéis e scripts do laboratório.

- [ ] **8.1 RPO e RTO** (`lesson_36_rpo_rto` / `topic_rpo_rto`)
  - *Resultado observável:* Definir RPO e RTO por serviço a partir do impacto na operação.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Refazer a análise para outro sistema crítico.
  - *Revisita:* Replicação (`topic_replicacao`).
- [ ] **8.2 Backup com Veeam e NetApp** (`lesson_37_backup` / `topic_backup`)
  - *Resultado observável:* Montar uma política de backup, executar um backup e provar a restauração.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Adaptar a política a outro RPO.
  - *Revisita:* RPO e RTO (`topic_rpo_rto`).
- [ ] **8.3 Monitoramento com Zabbix** (`lesson_38_zabbix` / `topic_zabbix`)
  - *Resultado observável:* Instalar o Zabbix, monitorar servidores e serviços e definir alarmes que indiquem ação.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Criar monitoramento para outra camada.
  - *Revisita:* Serviços e logs (`topic_servicos_logs`).
- [ ] **8.4 Painéis com Grafana** (`lesson_39_grafana` / `topic_grafana`)
  - *Resultado observável:* Construir um painel que responda perguntas de operação sobre o laboratório.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Fazer um painel para outro público.
  - *Revisita:* Monitoramento com Zabbix (`topic_zabbix`).
- [ ] **8.5 Automação: PowerShell, Bash e Python** (`lesson_40_automacao` / `topic_automacao`)
  - *Resultado observável:* Escrever, testar e versionar scripts que verifiquem a saúde do laboratório.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Adaptar o script a outra verificação e a outra linguagem.
  - *Revisita:* Serviços e logs (`topic_servicos_logs`).

**Fechamento da fase:** explicação de 2 minutos em inglês sobre a entrega da fase.

### Fase 9 — Integração

**Entrega da fase:** Dossiê final do ICC Linha Aurora.

- [ ] **9.1 Arquitetura ICC escalável e redundante** (`lesson_41_arquitetura_icc` / `topic_arquitetura_icc`)
  - *Resultado observável:* Propor a arquitetura completa, com redundância e crescimento, e defender cada decisão.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Escalar a arquitetura para uma segunda linha.
  - *Revisita:* O que é um ICC: ATS, SCADA e segurança (`topic_icc_visao`).
- [ ] **9.2 Revisão de projeto e redução de defeitos** (`lesson_42_revisao_projeto` / `topic_revisao_projeto`)
  - *Resultado observável:* Conduzir uma revisão com lista de verificação, registrar defeitos e mostrar a correção.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Revisar um projeto que você não fez.
  - *Revisita:* Verificação e validação (`topic_vv`).
- [ ] **9.3 Documentação e melhoria contínua** (`lesson_43_documentacao` / `topic_documentacao_colaboracao`)
  - *Resultado observável:* Entregar o dossiê navegável e uma apresentação técnica que outra pessoa consiga usar.
  - *Evidências exigidas:* Feynman e aplicação padrão.
  - *Transferência:* Ensinar uma parte do dossiê a outra pessoa e aplicar o retorno.
  - *Revisita:* Revisão de projeto e redução de defeitos (`topic_revisao_projeto`).

**Fechamento da fase:** explicação de 2 minutos em inglês sobre a entrega da fase.
