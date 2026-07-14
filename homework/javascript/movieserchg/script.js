const API_KEY = 'b916db5c';
const API_URL = 'https://www.omdbapi.com/';

let currentQuery = '';
let currentType = '';

const searchForm = document.getElementById('searchForm');
const titleInput = document.getElementById('titleInput');
const typeSelect = document.getElementById('typeSelect');
const resultsContainer = document.getElementById('results');
const paginationContainer = document.getElementById('pagination');

const modalOverlay = document.getElementById('modalOverlay');
const modalBody = document.getElementById('modalBody');
const modalCloseBtn = document.getElementById('modalCloseBtn');


searchForm.addEventListener('submit', function(e) {
    e.preventDefault();
    currentQuery = titleInput.value.trim();
    currentType = typeSelect.value;

    if (currentQuery) {
        searchMovies(1);
    }
});


resultsContainer.addEventListener('click', function(e) {
    
    const movieItem = e.target.closest('.movie-item');
    if (movieItem) {
        const imdbID = movieItem.getAttribute('data-id');
        if (imdbID) {
            showModal(imdbID);
        }
    }
});

paginationContainer.addEventListener('click', function(e) {
    const btn = e.target.closest('.page-btn');
    if (btn) {
        const page = btn.getAttribute('data-page');
        searchMovies(page);
        resultsContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
});

function showModal(imdbID) {
    modalOverlay.classList.add('visible');
    document.body.style.overflow = 'hidden';
    modalBody.innerHTML = '<p class="loading-text">Загрузка...</p>';
    fetchDetails(imdbID);
}

function hideModal() {
    modalOverlay.classList.remove('visible');
    document.body.style.overflow = '';
}

modalCloseBtn.addEventListener('click', hideModal);

modalOverlay.addEventListener('click', function(e) {
    if (e.target === modalOverlay) {
        hideModal();
    }
});

document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && modalOverlay.classList.contains('visible')) {
        hideModal();
    }
});


async function searchMovies(page) {
    const params = new URLSearchParams({
        s: currentQuery,
        type: currentType,
        page: page,
        apiKey: API_KEY
    });

    try {
        const response = await fetch(API_URL + '?' + params);
        const data = await response.json();

        if (data.Response === 'True') {
            renderResults(data.Search);
            renderPagination(page, parseInt(data.totalResults, 10));
        } else {
            resultsContainer.innerHTML = '<p class="not-found">Movie not found!</p>';
            paginationContainer.innerHTML = '';
        }
    } catch (error) {
        resultsContainer.innerHTML = '<p class="not-found">Ошибка при запросе к API.</p>';
        paginationContainer.innerHTML = '';
    }
}


function renderResults(movies) {
    let html = '';
    for (let i = 0; i < movies.length; i++) {
        const movie = movies[i];
        const poster = movie.Poster !== 'N/A'
            ? movie.Poster
            : 'https://via.placeholder.com/80x120?text=No+Image';


        html += '<div class="movie-item" data-id="' + movie.imdbID + '">'
            + '<img src="' + poster + '" alt="' + movie.Title + '" onerror="this.src=\'https://via.placeholder.com/80x120?text=No+Image\'">'
            + '<div class="movie-info">'
            + '<h3>' + movie.Title + ' <span>(' + movie.Year + ')</span></h3>'
            + '<p class="movie-type">Type: ' + movie.Type + '</p>'
            + '<button type="button" class="btn-details">Details</button>'
            + '</div>'
            + '</div>';
    }
    resultsContainer.innerHTML = html;
}


function renderPagination(currentPage, totalResults) {
    const totalPages = Math.ceil(totalResults / 10);
    let html = '';

    const startPage = Math.max(1, currentPage - 2);
    const endPage = Math.min(totalPages, startPage + 4);

    if (currentPage > 1) {
        html += '<button type="button" class="page-btn" data-page="' + (currentPage - 1) + '">&lt;</button>';
    }

    for (let i = startPage; i <= endPage; i++) {
        const cls = i === currentPage ? 'page-btn active' : 'page-btn';
        html += '<button type="button" class="' + cls + '" data-page="' + i + '">' + i + '</button>';
    }

    if (currentPage < totalPages) {
        html += '<button type="button" class="page-btn" data-page="' + (currentPage + 1) + '">&gt;</button>';
    }

    paginationContainer.innerHTML = html;
}

async function fetchDetails(imdbID) {
    const params = new URLSearchParams({
        i: imdbID,
        plot: 'full',
        apiKey: API_KEY
    });

    try {
        const response = await fetch(API_URL + '?' + params);
        const movie = await response.json();

        if (movie.Response === 'True') {
            modalBody.innerHTML =
                '<h2>' + movie.Title + '</h2>'
                + '<p><strong>Released:</strong> ' + movie.Released + '</p>'
                + '<p><strong>Genre:</strong> ' + movie.Genre + '</p>'
                + '<p><strong>Country:</strong> ' + movie.Country + '</p>'
                + '<p><strong>Director:</strong> ' + movie.Director + '</p>'
                + '<p><strong>Writer:</strong> ' + movie.Writer + '</p>'
                + '<p><strong>Actors:</strong> ' + movie.Actors + '</p>'
                + '<p><strong>Awards:</strong> ' + movie.Awards + '</p>'
                + '<p><strong>Plot:</strong> ' + movie.Plot + '</p>';
        } else {
            modalBody.innerHTML = '<p class="not-found">Не удалось загрузить информацию.</p>';
        }
    } catch (error) {
        modalBody.innerHTML = '<p class="not-found">Ошибка при запросе к API.</p>';
    }
}