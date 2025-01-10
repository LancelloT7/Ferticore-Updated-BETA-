// base.js

function toggleSidebar() {
    var sidebar = document.getElementById('sidebar');
    var content = document.getElementById('content');
    var toggleBtn = document.querySelector('.toggle-btn');

    // Alternar a classe 'hidden' na sidebar e 'shifted' no conteúdo
    sidebar.classList.toggle('hidden');
    content.classList.toggle('shifted');

    // Ajustar a posição do botão conforme a visibilidade da sidebar
    if (sidebar.classList.contains('hidden')) {
        toggleBtn.style.left = '10px'; // Colocar o botão à esquerda quando a sidebar estiver escondida
    } else {
        toggleBtn.style.left = '260px'; // Colocar o botão ao lado da sidebar quando estiver visível
    }
}
