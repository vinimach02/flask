    <script>
        // Função para quebrar texto em uma célula quando encontra uma palavra que começa com "hom"
        function quebrarTexto() {
            var tabela = document.getElementById('minhaTabela');
            var linhas = tabela.getElementsByTagName('tr');

            for (var i = 0; i < linhas.length; i++) {
                var celulas = linhas[i].getElementsByTagName('td');

                for (var j = 0; j < celulas.length; j++) {
                    var texto = celulas[j].textContent;

                    // Quebra o texto na célula onde encontrar uma palavra que começa com "hom"
                    var partes = texto.split(/(\bhom\w*\b)/i);
                    var novoHTML = '';

                    for (var k = 0; k < partes.length; k++) {
                        if (partes[k].toLowerCase().startsWith('hom')) {
                            novoHTML += '<br>' + partes[k];
                        } else {
                            novoHTML += partes[k];
                        }
                    }

                    celulas[j].innerHTML = novoHTML;
                }
            }
        }

        // Chama a função quando a página é carregada
        window.onload = quebrarTexto;
    </script>
