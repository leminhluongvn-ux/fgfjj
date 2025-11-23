total_modified = sum('✅' in entry for entry in log_entries)
    summary = f"🔧 Tổng số file đã sửa: {total_modified}"
    print(summary)
    log_entries.append(summary)

    # Ghi log với timestamp
    with open("log_patch_runtime.txt", "w", encoding="utf-8") as log_file:
        log_file.write(f"--- Log chạy lúc {datetime.now()} ---\n")
