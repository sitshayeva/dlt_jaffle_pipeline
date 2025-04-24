# 🚀 Jaffle Shop API Data Pipeline with DLT

This repository contains a high-performance data pipeline built using [`dlt`](https://dlthub.com/) (Data Load Tool) to extract data from the **public Jaffle Shop API**, transform it, and load it into a **DuckDB** database.

✅ Deployed via **GitHub Actions**  
✅ Fully scheduled (runs every 30 minutes)  
✅ Optimized with performance techniques: **chunking**, **parallelism**, **buffer control**, and more!

---

## 📦 Technologies

- [`dlt`](https://github.com/dlt-hub/dlt): Modern Python data pipeline framework
- `DuckDB`: In-process OLAP SQL engine
- `pandas`: For data preview and quick analysis
- `GitHub Actions`: CI/CD orchestration for deployment

---

## 📁 Project Structure

```bash
.
├── pipeline.py                  # Main pipeline script (DLT + DuckDB)
├── requirements.txt            # Dependencies for local development
├── .github/
│   └── workflows/
│       └── run_jaffle_pipeline.yml  # Auto-generated GitHub Actions workflow
└── README.md
```

---

## ⚙️ How It Works

The pipeline extracts data from:
```
https://jaffle-shop.scalevector.ai/api/v1/orders
```

It:
- Uses `ordered_at` as an incremental cursor
- Fetches only orders with `order_total <= 500`
- Stores them in a DuckDB file in your Google Drive or local path

---

## 🚀 Running Locally

```bash
# Create and activate a virtual environment
python -m venv .venv && source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python pipeline.py
```

You’ll find your `jaffle_shop_pipeline.duckdb` file created in the configured location (e.g., Google Drive).

---

## ☁️ GitHub Actions Deployment

This project is already configured for GitHub Actions.

To update or redeploy:

```bash
# Install dlt CLI
pip install "dlt[cli]"

# (Optional) Run and verify pipeline
python pipeline.py

# Deploy (generates .github workflow + secret list)
dlt deploy pipeline.py github-action --schedule "*/30 * * * *"
```

➡️ Copy the printed secrets into:  
**GitHub → Settings → Secrets → Actions**

---

## 🔍 Sample Output Query

Once data is loaded, you can connect to DuckDB and run:

```sql
SELECT * FROM jaffle_data.orders LIMIT 10;
```

---

## 📅 Scheduled Runs

| Cron           | Trigger Time         |
|----------------|----------------------|
| `"0 0 * * *"` | Daily    |

You can monitor the job via:  
[**GitHub Actions → Workflows**](./.github/workflows/run_jaffle_pipeline.yml)

---

## 📬 Contact / Issues

If you have questions or run into problems, feel free to open an issue or reach out through [dltHub Discussions](https://github.com/dlt-hub/dlt/discussions).

---

## 🧠 Credits

- Built with ❤️ using [dlt](https://dlthub.com)
- Public API provided by [Jaffle Shop Demo](https://jaffle-shop.scalevector.ai)
