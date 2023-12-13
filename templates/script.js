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
