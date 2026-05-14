let selectedTicketId = null
let bsModal = null

const COLORS = { 1: 'danger', 2: 'warning', 3: 'info', 4: 'success' }

document.addEventListener('DOMContentLoaded', () => {
    bsModal = new bootstrap.Modal(document.getElementById('modal'))
    loadQueue()
    loadHistory()
})

document.getElementById('ticket-form').addEventListener('submit', async (e) => {
    e.preventDefault()
    const res = await fetch('/tickets', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            client: document.getElementById('client').value.trim(),
            description: document.getElementById('description').value.trim(),
            priority: parseInt(document.getElementById('priority').value)
        })
    })
    if (res.ok) { document.getElementById('ticket-form').reset(); loadQueue() }
})

function ticketCard(t, showUpdate = false) {
    return `
        <div class="d-flex justify-content-between align-items-center border-start border-4 border-${COLORS[t.priority]} bg-white rounded p-3 mb-2 shadow-sm">
            <div>
                <small class="text-muted">${t.ticket_id}</small>
                <div class="fw-semibold">${t.client}</div>
                <small class="text-secondary">${t.description}</small>
                ${showUpdate ? `<br><button class="btn btn-outline-secondary btn-sm mt-1" onclick="openModal('${t.ticket_id}', ${t.priority})">Actualizar prioridad</button>` : ''}
            </div>
            <span class="badge bg-${COLORS[t.priority]}">${t.priority_label}</span>
        </div>`
}

async function loadQueue() {
    const data = await fetch('/tickets').then(r => r.json())
    document.getElementById('total').textContent = data.total
    document.getElementById('queue-list').innerHTML = data.tickets.length
        ? data.tickets.map(t => ticketCard(t, true)).join('')
        : '<p class="text-muted text-center">No hay tickets en cola.</p>'
}

async function attendNext() {
    const res = await fetch('/tickets/next', { method: 'DELETE' })
    if (!res.ok) { alert('La cola está vacía.'); return }
    loadQueue(); loadHistory()
}

async function searchTicket() {
    const id = document.getElementById('search-id').value.trim()
    const resultDiv = document.getElementById('search-result')
    if (!id) return
    const res = await fetch(`/tickets/${id}`)
    resultDiv.innerHTML = res.ok
        ? ticketCard(await res.json())
        : '<p class="text-danger small">Ticket no encontrado.</p>'
}

async function loadHistory() {
    const data = await fetch('/history').then(r => r.json())
    document.getElementById('history-list').innerHTML = data.history.length
        ? [...data.history].reverse().map(t => `
            <div class="border-bottom py-2">
                <small class="text-muted">${t.ticket_id} · ${t.priority_label}</small>
                <div class="fw-semibold">${t.client}</div>
                <small class="text-secondary">${t.description}</small>
            </div>`).join('')
        : '<p class="text-muted text-center">No hay tickets atendidos.</p>'
}

function openModal(ticketId, currentPriority) {
    selectedTicketId = ticketId
    document.getElementById('modal-ticket-id').textContent = ticketId
    document.getElementById('modal-priority').value = currentPriority
    bsModal.show()
}

function closeModal() { bsModal.hide(); selectedTicketId = null }

async function confirmUpdate() {
    const res = await fetch(`/tickets/${selectedTicketId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ priority: parseInt(document.getElementById('modal-priority').value) })
    })
    if (res.ok) { closeModal(); loadQueue() }
}