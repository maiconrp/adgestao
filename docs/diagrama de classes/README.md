# `DOCS` Diagrama de Classes - AD Gestão

Este diagrama de classes foi criado como parte do projeto [AD Gestão][adgestao], com o objetivo de fornecer uma representação visual das classes e relações existentes no sistema.

## 📃 Descrição
<p align=justify> :information_source: O diagrama de classes mostra as classes principais do sistema, bem como suas relações e dependências. Ele é útil para entender a estrutura do código e como as diferentes classes trabalham juntas para implementar as funcionalidades do sistema. </p>

## Conteúdo
* **`Classes`**: lista e descrição das classes principais do sistema.
* **`Atributos`**: lista dos atributos de cada classe, incluindo o tipo e a visibilidade.
* **`Métodos`**: lista dos métodos de cada classe, incluindo a assinatura e a visibilidade.
* **`Relações`**: representação visual das relações entre as classes, incluindo associações, agregações e heranças.

## Visão Geral das Classes

| Classe              	| Descrição                                                                                                                             	|
|:---------------------	|:---------------------------------------------------------------------------------------------------------------------------------------	|
| Usuario             	| Classe responsável por armazenar informações de cadastro de usuários do sistema, como nome, email, cpf e senha.                       	|
| Tesoureiro          	| Classe que representa o usuário responsável por gerenciar as finanças da igreja em que atua.                                          	|
| Igreja              	| Classe que armazena informações sobre uma igreja, como localização, nome e tesoureiro local.                                          	|
| TesoureiroSede      	| Classe que representa o usuário responsável por avaliar e autorizar ou negar os pedidos de cadastro de usuários.                      	|
| Pastor              	| Classe que representa o usuário responsável por liderar uma igreja.                                                                   	|
| Saida               	| Classe que armazena informações sobre as saídas financeiras de uma igreja, como data, descrição, valor e assinatura do tesoureiro.    	|
| Oferta              	| Classe que armazena informações sobre as ofertas financeiras de uma igreja, como data, tipo de culto e valor total.                   	|
| Dizimo              	| Classe que armazena informações sobre os dízimos de uma igreja, como data, contribuinte e valor.                                      	|
| Membro              	| Classe que armazena informações sobre os membros de uma igreja, como nome, data de adesão e contribuição mensal.                      	|
| RelatorioMensal     	| Classe que armazena informações sobre os relatórios financeiros mensais de uma igreja, incluindo gráficos e relatórios de tendências. 	|
| RelatorioGeral      	| Classe que armazena informações sobre os relatórios financeiros gerais de uma igreja, incluindo gráficos e relatórios de tendências.  	|
| Entradas            	| Classe que armazena informações sobre as entradas financeiras de uma igreja, incluindo os dízimos e as ofertas.                       	|
| Saidas              	| Classe que armazena informações sobre as saídas financeiras de uma igreja.                                                            	|
| SolicitacaoCadastro 	| Classe que armazena informações sobre os pedidos de cadastro de usuários, incluindo nome, email, cpf, senha e igreja em que atuam.    	|
|                     	|                                                                                                                                       	|

## Utilização
<p align=justify> Este diagrama deve ser utilizado como uma ferramenta de referência durante o desenvolvimento do projeto. Ele pode ser atualizado à medida que novas classes e relações forem adicionadas ou modificadas. Ele também pode ser usado para comunicar a estrutura do código para outros membros do time de desenvolvimento e para documentação do sistema.<p>

## Observações
Este diagrama foi criado usando a ferramenta [StarUML][StarUML], mas pode ser visualizado e editado usando **outras ferramentas de modelagem de classes**, como o [MicrosoftVisio][MicrosoftVisio] ou o [SmartDraw][SmartDraw]. É importante lembrar que este diagrama é apenas uma **representação visual da estrutura do código** e pode não incluir todos os detalhes e nuances do sistema. Ele deve ser usado em conjunto com **outras documentações** e **diagramas**, além da pesquisa e análise para obter uma compreensão completa do projeto.

[adgestao]: https://github.com/maiconrp/adgestao
[StarUML]: http://staruml.io/
[MicrosoftVisio]: https://products.office.com/en-us/visio/flowchart-software
[SmartDraw]: https://www.smartdraw.com/class-diagram/
