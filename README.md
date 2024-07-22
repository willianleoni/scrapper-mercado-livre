# Mercado Livre Scraper

Este projeto é um scraper para o Mercado Livre que extrai detalhes dos produtos de uma URL fornecida, organiza os dados em um DataFrame do pandas e salva os resultados em um arquivo Excel formatado.

## Funcionalidades

- Extrai informações de produtos de uma URL do Mercado Livre.
- Navega automaticamente pelas páginas de resultados.
- Organiza os dados em um DataFrame do pandas.
- Calcula e adiciona uma coluna de desconto.
- Salva os dados em um arquivo Excel com formatação.
- Abre o arquivo Excel automaticamente após a execução.

## Dependências

- Python 3.x
- pandas
- openpyxl
- requests
- BeautifulSoup4

### Arquivos Principais

- **main.py**: O ponto de entrada principal do scraper.
- **dataframe.py**: Contém a classe `DataFrameHandler` para manipulação e formatação de dados.
- **extractor.py**: Contém a classe `ProductDetailsExtractor` para extração de dados dos produtos.
- **scrapper.py**: Contém a classe `MercadoLivreScraper` para buscar e navegar nas páginas.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
