# `DOCS` Diagrama de Casos de Uso - AD Gestão

Este diagrama de casos de uso foi criado como parte do projeto [AD Gestão][adgestao], com o objetivo de fornecer uma representação visual dos casos de uso e das interações entre os atores e o sistema.

## 📃 Descrição
<p align=justify> :information_source: O diagrama de casos de uso mostra os casos de uso principais do sistema, bem como as interações entre os atores e o sistema. Ele é útil para entender as funcionalidades do sistema e como os usuários interagem com ele.</p>

## Conteúdo
* **`Casos de uso`**: lista e descrição dos casos de uso principais do sistema.
* **`Atores`**: lista dos atores envolvidos nos casos de uso, incluindo o papel de cada um.
* **`Relações`**: representação visual das relações entre os casos de uso e os atores, incluindo inclusão, extensão e generalização.

## Visão Geral dos Atores
| Ator          | Descrição|
|:--------------|:---------|
| Usuário       | Ator principal do sistema, com funções básicas como login e solicitação de cadastro. Eles são os usuários comuns do sistema.
| Pastor        | Especialização de usuário com função de visualizar relatórios e autorizar ações do tesoureiro. Ele é responsável por liderar uma igreja.
| Tesoureiro    | Especialização de usuário com funções de tesoureiro na sua igreja local, responsável por gerenciar as finanças da igreja.
| TesoureiroSede| Especialização de tesoureiro com funções de administração e gerenciamento de usuários, igrejas, entre outros aspectos do sistema. Ele é responsável por avaliar e autorizar ou negar os pedidos de cadastro de usuários.
## Utilização
<p align=justify> Este diagrama deve ser utilizado como uma ferramenta de referência durante o desenvolvimento do projeto. Ele pode ser atualizado à medida que novos casos de uso e relações forem adicionados ou modificadas. Ele também pode ser usado para comunicar as funcionalidades do sistema para outros membros do time de desenvolvimento e para documentação do sistema.<p>

## Observações
Este diagrama foi criado usando a ferramenta [StarUML][StarUML], mas pode ser visualizado e editado usando **outras ferramentas de modelagem de classes**, como o [MicrosoftVisio][MicrosoftVisio] ou o [SmartDraw][SmartDraw]. É importante lembrar que este diagrama é apenas uma **representação visual da estrutura do código** e pode não incluir todos os detalhes e nuances do sistema. Ele deve ser usado em conjunto com **outras documentações** e **diagramas**, além da pesquisa e análise para obter uma compreensão completa do projeto.

[adgestao]: https://github.com/maiconrp/adgestao
[StarUML]: http://staruml.io/
[MicrosoftVisio]: https://products.office.com/en-us/visio/flowchart-software
[SmartDraw]: https://www.smartdraw.com/class-diagram/




