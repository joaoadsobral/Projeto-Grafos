# Projeto: Algoritmos - Grupo #2.4

## Disciplina
- **Disciplina:** Algoritmos
- **Docente:** Sérgio Queiroz

## Participantes
- João Antônio
- Gabriel Mendonça

## Relatório do Projeto

### Contexto do Problema
Considerando a vasta quantidade de bairros em Recife, propusemos a construção de uma base de dados utilizando os bairros como vértices e as distâncias entre eles como arestas. Isso tornaria o problema mais tangível, facilitando sua compreensão. Nossa base de dados contém informações sobre os bairros, seus vizinhos e suas localizações geográficas.

### Implementação
- **Algoritmo Utilizado:** Bellman-Ford, um algoritmo de caminho mais curto utilizado para encontrar a rota mais curta entre um nó de origem e um nó de destino em um grafo direcionado ponderado.
- **Desenvolvimento:** Inicialmente, estudamos o assunto para entender como aplicar nossa ideia em forma de código. Começamos criando a base de dados para facilitar a manipulação. Após pesquisa e trabalho, desenvolvemos o código. Extraímos informações da planilha e, utilizando o algoritmo de Bellman-Ford, geramos o menor caminho entre dois pontos, considerando a movimentação entre os bairros vizinhos. Em seguida, criamos um visualizador de grafos para representar graficamente o caminho encontrado, juntamente com uma interface gráfica simples para integrar tudo.
- **Bibliotecas Utilizadas:**
  - `openpyxl`: Para abrir e extrair informações da planilha.
  - `geopy.distance`: Para transformar distâncias geográficas de latitude e longitude em quilômetros.
  - `matplotlib.pyplot` e `networkx`: Para gerar o visualizador de grafos e destacar o caminho entre os dois vértices.
  - `tkinter`: Para criar a interface gráfica.

### Conclusão
Após clonar o repositório e instalar as bibliotecas necessárias, basta executar o programa e dará de cara com uma tela pedindo pra inserir uma origem e um destino. Onde você deverá preencher com 2 Bairros de Recife Onde terá como resultado o menor caminho entre esses 2 pontos demonstrado, além da distância entre cada um desses bairros vizinhos e a quilometragem final. Além disso, gera um Grafo que demonstra por completo os vértices e suas distâncias por meio das arestas, e além disso, e em vermelho, destaca o caminho citado na interface gráfica, para encerrar o programa, deve apenas fechar as 2 abas. Se você enviar dois caminhos seguidos, sem fechar a aba do grafo, acabará gerando o grafo com 2 caminhos destacados. Não aperte calcular caminho 2 vezes para mesma rota, pois sobrecarregará o programa e acabará duplicando o grafo.

Porém, caso você digite alguma origem ou destino incorreto (verificar lista de bairros na planilha do excel), dará de cara com ua tela de erro pedindo pra inserir novamente
Após isso, você pode tentar novamente para gerar um resultado possível.


