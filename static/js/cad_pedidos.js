document.getElementById('adicionar-produto').addEventListener('click', function() {
    var produtoSelect = document.getElementById('produto');
    var quantidadeInput = document.getElementById('quantidade');
    var produtoId = produtoSelect.value;
    var produtoNome = produtoSelect.options[produtoSelect.selectedIndex].getAttribute('data-nome');
    var produtoPreco = produtoSelect.options[produtoSelect.selectedIndex].getAttribute('data-preco');
    var quantidade = quantidadeInput.value;

    // Verifica se a quantidade é válida
    if (quantidade <= 0 || !quantidade) {
        alert('Por favor, insira uma quantidade válida.');
        return;
    }

    if (produtoId) {
        var produtosSelecionadosDiv = document.getElementById('produtos-selecionados');

        // Verifica se o produto já foi adicionado
        var produtoExistente = document.querySelector(`input[name="produto"][value="${produtoId}"]`);

        if (!produtoExistente) {
            // Cria o item visual do produto
            var novoItem = document.createElement('div');
            novoItem.className = 'produto-item';
            novoItem.textContent = produtoNome + ' - ' + quantidade + ' toneladas';

            // Cria o botão de remoção
            var removerBtn = document.createElement('button');
            removerBtn.type = 'button';
            removerBtn.textContent = 'Remover';
            removerBtn.onclick = function() {
                produtosSelecionadosDiv.removeChild(novoItem);  // Remove o item do cartão
                produtosSelecionadosDiv.removeChild(inputHiddenProduto);  // Remove o campo oculto do produto
                produtosSelecionadosDiv.removeChild(inputHiddenQuantidade);  // Remove o campo oculto da quantidade
            };

            novoItem.appendChild(removerBtn);
            produtosSelecionadosDiv.appendChild(novoItem);

            // Cria um campo hidden para enviar o produto selecionado com a quantidade
            var inputHiddenProduto = document.createElement('input');
            inputHiddenProduto.type = 'hidden';
            inputHiddenProduto.name = 'produto';  // Nome da lista de produtos que será enviada
            inputHiddenProduto.value = produtoId;

            var inputHiddenQuantidade = document.createElement('input');
            inputHiddenQuantidade.type = 'hidden';
            inputHiddenQuantidade.name = 'quantidade';  // Nome da lista de quantidades
            inputHiddenQuantidade.value = quantidade;

            produtosSelecionadosDiv.appendChild(inputHiddenProduto);
            produtosSelecionadosDiv.appendChild(inputHiddenQuantidade);
        } else {
            alert("Este produto já foi adicionado.");
        }
    }
});
