function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const content = document.getElementById('content');
    const toggleButton = document.querySelector('.toggle-btn');

    // Adicionar ou remover a classe 'hidden' da sidebar
    sidebar.classList.toggle('hidden');

    // Adicionar ou remover a classe 'shifted' do conteúdo
    content.classList.toggle('shifted');

    // Ajustar a posição do botão
    if (sidebar.classList.contains('hidden')) {
        toggleButton.style.left = '10px'; // Ajusta o botão para a posição inicial
    } else {
        toggleButton.style.left = '260px'; // Ajusta o botão para a posição da sidebar visível
    }
}
