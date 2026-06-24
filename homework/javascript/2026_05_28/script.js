let colors = [];

const nameInput = document.getElementById('colorName');
const typeSelect = document.getElementById('colorType');
const codeInput = document.getElementById('colorCode');
const saveBtn = document.getElementById('saveBtn');
const nameError = document.getElementById('nameError');
const codeError = document.getElementById('codeError');
const paletteContainer = document.getElementById('paletteContainer');

const THREE_HOURS_MS = 3 * 60 * 60 * 1000;

function saveToStorage() {
    const payload = {
        data: colors,
        timestamp: Date.now()
    };
    localStorage.setItem('colorsData', JSON.stringify(payload));
}

function loadFromStorage() {
    const stored = localStorage.getItem('colorsData');
    if (!stored) return false;
    try {
        const parsed = JSON.parse(stored);
        if (Date.now() - parsed.timestamp < THREE_HOURS_MS) {
            colors = parsed.data;
            return true;
        } else {
            localStorage.removeItem('colorsData');
            return false;
        }
    } catch (e) {
        return false;
    }
}

function validateName(name) {
    if (!name.trim()) return { ok: false, msg: "Название обязательно" };
    if (!/^[a-zA-Z]+$/.test(name)) return { ok: false, msg: "Только буквы (a-z, A-Z)" };
    if (colors.some(c => c.name.toLowerCase() === name.toLowerCase())) {
        return { ok: false, msg: "Такое название уже существует" };
    }
    return { ok: true };
}

function validateCode(code, type) {
    if (type === 'HEX') {
        if (!/^#[0-9A-Fa-f]{6}$/.test(code)) {
            return { ok: false, msg: "Формат: # и 6 символов (0-9, A-F)" };
        }
    } else {
        const parts = code.split(',').map(p => p.trim());
        const nums = parts.map(Number);
        if (parts.length !== (type === 'RGBA' ? 4 : 3) || nums.some(isNaN)) {
            return { ok: false, msg: `Введите ${type === 'RGBA' ? 4 : 3} числа через запятую` };
        }
        if (nums.slice(0, 3).some(n => n < 0 || n > 255)) {
            return { ok: false, msg: "Числа должны быть от 0 до 255" };
        }
        if (type === 'RGBA' && (nums[3] < 0 || nums[3] > 1)) {
            return { ok: false, msg: "Последнее число (прозрачность) от 0 до 1" };
        }
    }
    return { ok: true };
}

function renderPalette() {
    paletteContainer.innerHTML = '';
    if (colors.length === 0) {
        paletteContainer.innerHTML = '<div class="no-colors">Список цветов пуст</div>';
        return;
    }
    colors.forEach(c => {
        const card = document.createElement('div');
        card.className = 'color-card';
        let bg = c.code;
        if (c.type === 'RGB') bg = `rgb(${c.code})`;
        if (c.type === 'RGBA') bg = `rgba(${c.code})`;
        card.style.backgroundColor = bg;

        card.innerHTML = `
            <span>${c.name}</span>
            <span style="font-weight:normal;">${c.type}</span>
            <span style="font-weight:normal;">${c.code}</span>
        `;
        paletteContainer.appendChild(card);
    });
}

function addColor() {
    nameError.textContent = '';
    codeError.textContent = '';

    const name = nameInput.value.trim();
    const type = typeSelect.value;
    const code = codeInput.value.trim();

    const nameCheck = validateName(name);
    if (!nameCheck.ok) {
        nameError.textContent = nameCheck.msg;
    }

    const codeCheck = validateCode(code, type);
    if (!codeCheck.ok) {
        codeError.textContent = codeCheck.msg;
    }

    if (!nameCheck.ok || !codeCheck.ok) return;

    colors.push({ name, type, code });
    saveToStorage();
    renderPalette();

    nameInput.value = '';
    codeInput.value = '';
    nameInput.focus();
}

function init() {
    const loaded = loadFromStorage();
    if (!loaded) colors = []; // Явно обнуляем, если в хранилище ничего нет или срок истек
    renderPalette();
}

saveBtn.addEventListener('click', addColor);
init();