// Scroll fade-in effect
window.addEventListener('scroll', () => {
    document.querySelectorAll('.fade-in').forEach(el => {
        const rect = el.getBoundingClientRect();
        if(rect.top < window.innerHeight - 100){
            el.classList.add('visible');
        }
    });
});

// Simulateur de coût
const employeesInput = document.getElementById('employees');
const planSelect = document.getElementById('plan');
const periodInput = document.getElementById('period');
const totalDisplay = document.getElementById('total');

function updateTotal() {
    const employees = parseInt(employeesInput.value) || 0;
    const period = parseInt(periodInput.value) || 0;
    const plan = planSelect.value;
    let price = plan === 'basique' ? 15000 : 25000;
    const total = employees * price * period;
    totalDisplay.textContent = total.toLocaleString('fr-FR') + ' Ar';
}

employeesInput.addEventListener('input', updateTotal);
planSelect.addEventListener('change', updateTotal);
periodInput.addEventListener('input', updateTotal);
updateTotal();
