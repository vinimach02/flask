<script>
    $(document).ready(function() {
        // Quando o dropdown principal é alterado
        $('#opcoes').change(function() {
            var opcaoSelecionada = $(this).val();

            // Executa a ação no backend
            $.ajax({
                type: 'POST',
                url: '/executar_acao',
                data: { opcoes: opcaoSelecionada },
                success: function(resultado) {
                    console.log(resultado);
                    // Aqui você pode fazer algo com o resultado se necessário
                },
                error: function(error) {
                    console.error('Erro ao realizar a chamada AJAX:', error);
                }
            });
        });
    });
</script>
        $(document).ready(function() {
            $("#dropdown1").change(function() {
                var valorDropdown1 = $(this).val();
                
                // Enviar uma requisição assíncrona para atualizar o dropdown2
                $.post("/atualizar_dropdown2", { valor_dropdown1: valorDropdown1 }, function(data) {
                    preencherDropdown2(data.opcoes_dropdown2);
                });
            });

            function preencherDropdown2(opcoesDropdown2) {
                $("#dropdown2").empty();  // Limpar opções atuais

                $.each(opcoesDropdown2, function(index, opcao) {
                    $("#dropdown2").append('<option value="' + opcao + '">' + opcao + '</option>');
                });
            }
        });