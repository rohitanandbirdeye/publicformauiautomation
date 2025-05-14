document.addEventListener('DOMContentLoaded', () => {
  // Navigation
  const navRun = document.getElementById('nav-run');
  const navResults = document.getElementById('nav-results');
  const runSection = document.getElementById('run-section');
  const resultsSection = document.getElementById('results-section');

  function showSection(section) {
    if (section === 'run') {
      runSection.classList.remove('d-none');
      resultsSection.classList.add('d-none');
      navRun.classList.add('active');
      navResults.classList.remove('active');
    } else {
      runSection.classList.add('d-none');
      resultsSection.classList.remove('d-none');
      navRun.classList.remove('active');
      navResults.classList.add('active');
      fetchAutomationResults();
    }
  }

  navRun.addEventListener('click', (e) => {
    e.preventDefault();
    showSection('run');
  });
  navResults.addEventListener('click', (e) => {
    e.preventDefault();
    showSection('results');
  });

  // Run Automation Logic
  const automationSelect = document.getElementById('automation-select');
  const runBtn = document.getElementById('run-btn');
  const runLoading = document.getElementById('run-loading');
  const runStatus = document.getElementById('run-status');

  // Enable/disable run button based on dropdown value
  function updateRunButtonState() {
    runBtn.disabled = !automationSelect.value;
    runStatus.innerHTML = '';
  }

  // Initial check on page load
  updateRunButtonState();

  automationSelect.addEventListener('change', updateRunButtonState);

  runBtn.addEventListener('click', async () => {
    const value = automationSelect.value;
    if (!value) return;
    runBtn.disabled = true;
    runLoading.classList.remove('d-none');
    runStatus.innerHTML = '';
    let endpoint = '';
    if (value === 'dlc') endpoint = '/run-dlc';
    else if (value === 'reviewus') endpoint = '/run-reviewus';
    else if (value === 'checkin') endpoint = '/run-checkin';
    try {
      const response = await fetch(`http://127.0.0.1:8000${endpoint}`, { method: 'POST' });
      const data = await response.json();
      runStatus.innerHTML = `<div class="alert alert-success">${data.status || 'Task completed.'}</div>`;
    } catch (error) {
      runStatus.innerHTML = `<div class="alert alert-danger">Failed to run automation.</div>`;
      console.error(error);
    } finally {
      runLoading.classList.add('d-none');
      runBtn.disabled = false;
    }
  });

  // Results Table Logic
  const tableBody = document.getElementById('results-table');
  const resultsHeader = document.getElementById('automationresults');

  async function fetchAutomationResults() {
    tableBody.innerHTML = `<tr><td colspan="4" class="loading">Loading...</td></tr>`;
    try {
      const response = await fetch('http://127.0.0.1:8000/getAutomationResult');
      if (!response.ok) throw new Error('Network response was not ok');
      const data = await response.json();
      if (!data.results || !Array.isArray(data.results) || data.results.length === 0) {
        throw new Error('No results found');
      }
      tableBody.innerHTML = '';
      let rowCount = 0;
      data.results.forEach((run, idx) => {
        const { start, end, pages } = run;
        // Add a header row for each run
        const runHeaderRow = document.createElement('tr');
        runHeaderRow.innerHTML = `
          <td colspan="4" class="table-secondary fw-bold">
            Run #${data.results.length - idx} &mdash; ${new Date(start * 1000).toLocaleString()} - ${new Date(end * 1000).toLocaleString()}
          </td>
        `;
        tableBody.appendChild(runHeaderRow);
        Object.entries(pages).forEach(([page, details]) => {
          const row = document.createElement('tr');
          row.innerHTML = `
            <td>${page}</td>
            <td>${details.success ? "✅" : "❌"}</td>
            <td>${details.message}</td>
            <td>${new Date(start * 1000).toLocaleTimeString()}</td>
          `;
          tableBody.appendChild(row);
          rowCount++;
        });
      });
      resultsHeader.textContent = `Public forms automation results (${rowCount} entries)`;
    } catch (error) {
      tableBody.innerHTML = `
        <tr>
          <td colspan="4" class="text-danger text-center">Failed to fetch data from the server.</td>
        </tr>
      `;
      resultsHeader.textContent = "Automation Results (Error)";
      console.error(error);
    }
  }

  // Default view
  showSection('run');
});