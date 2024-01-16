    <script>
        // Função para quebrar linha quando a célula começa com "hom"
        function quebrarLinha() {
            var tabela = document.getElementById('minhaTabela');
            var linhas = tabela.getElementsByTagName('tr');

            for (var i = 0; i < linhas.length; i++) {
                var celula = linhas[i].getElementsByTagName('td')[0];

                if (celula && celula.textContent.trim().toLowerCase().startsWith('hom')) {
                    celula.innerHTML = 'Hom<br>' + celula.innerHTML;
                }
            }
        }

        // Chama a função quando a página carrega
        window.onload = quebrarLinha;
    </script>
