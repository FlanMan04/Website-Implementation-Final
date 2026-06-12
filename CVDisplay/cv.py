from pyscript import document, when
from js import localStorage, window, html2pdf
import json

def load():
    raw = localStorage.getItem("cv_data")
    if raw is None:
        # 10+ categories sample
        sample = [
            {"id":1,"category":"Personal","title":"John Doe","details":"email@example.com","visible":True},
            {"id":2,"category":"Work","title":"Dev at Corp","details":"2020-now","visible":True},
            {"id":3,"category":"Education","title":"BSc CS","details":"Univ 2015-2019","visible":True},
            {"id":4,"category":"Skills","title":"Python, JS","details":"","visible":True},
            {"id":5,"category":"Languages","title":"English (fluent)","details":"","visible":True},
            {"id":6,"category":"Certifications","title":"AWS","details":"2022","visible":True},
            {"id":7,"category":"Projects","title":"CV Manager","details":"PyScript","visible":True},
            {"id":8,"category":"Awards","title":"Hackathon","details":"2021","visible":True},
            {"id":9,"category":"Volunteering","title":"Mentor","details":"2020","visible":True},
            {"id":10,"category":"Publications","title":"Blog","details":"tech articles","visible":True},
            {"id":11,"category":"References","title":"Prof. Smith","details":"smith@univ","visible":True},
        ]
        localStorage.setItem("cv_data", json.dumps(sample))
        return sample
    return json.loads(raw)

def save(data):
    localStorage.setItem("cv_data", json.dumps(data))

entries = load()
next_id = max((e["id"] for e in entries), default=0) + 1

def render_all():
    # left panel
    html = ""
    for e in entries:
        cls = "hidden" if not e["visible"] else ""
        html += f'''
        <div class="entry {cls}" data-id="{e['id']}">
            <b>{e['title']}</b> <small>({e['category']})</small><br>
            {e['details'][:50]}<br>
            <button class="toggle">{"Hide" if e['visible'] else "Show"}</button>
            <button class="edit">Edit</button>
            <button class="delete">Delete</button>
        </div>
        '''
    document.getElementById("entriesList").innerHTML = html

    groups = {}
    for e in entries:
        if not e["visible"]: continue
        groups.setdefault(e["category"], []).append(e)
    resume_html = ""
    for cat, items in groups.items():
        resume_html += f"<div class='resume-section'><strong>{cat}</strong><ul>"
        for it in items:
            resume_html += f"<li><b>{it['title']}</b><br>{it['details']}</li>"
        resume_html += "</ul></div>"
    document.getElementById("resumeContainer").innerHTML = resume_html or "<p>No visible entries.</p>"

    js_code = """
        document.querySelectorAll('.toggle').forEach(btn => {
            btn.onclick = () => window.toggle(parseInt(btn.parentElement.getAttribute('data-id')));
        });
        document.querySelectorAll('.edit').forEach(btn => {
            btn.onclick = () => window.edit(parseInt(btn.parentElement.getAttribute('data-id')));
        });
        document.querySelectorAll('.delete').forEach(btn => {
            btn.onclick = () => window.del(parseInt(btn.parentElement.getAttribute('data-id')));
        });
    """
    window.eval(js_code)

def add_entry(ev=None):
    global next_id
    cat = document.getElementById("cat").value
    title = document.getElementById("title").value.strip()
    details = document.getElementById("details").value.strip()
    visible = document.getElementById("visible").value == "true"
    if not title:
        window.alert("Title required")
        return
    entries.append({"id": next_id, "category": cat, "title": title, "details": details, "visible": visible})
    next_id += 1
    save(entries)
    render_all()
    # clear form
    document.getElementById("title").value = ""
    document.getElementById("details").value = ""

def toggle_visible(entry_id):
    for e in entries:
        if e["id"] == entry_id:
            e["visible"] = not e["visible"]
            break
    save(entries)
    render_all()

def edit_entry(entry_id):
    for e in entries:
        if e["id"] == entry_id:
            new_title = window.prompt("New title:", e["title"])
            if new_title is not None: e["title"] = new_title
            new_details = window.prompt("New details:", e["details"])
            if new_details is not None: e["details"] = new_details
            new_cat = window.prompt("New category:", e["category"])
            if new_cat is not None: e["category"] = new_cat
            break
    save(entries)
    render_all()

def delete_entry(entry_id):
    if window.confirm("Delete entry?"):
        global entries
        entries = [e for e in entries if e["id"] != entry_id]
        save(entries)
        render_all()

def generate_pdf(ev=None):
    el = document.getElementById("resumeContainer")
    html2pdf().from(el).save()

# Expose to JS
window.toggle = toggle_visible
window.edit = edit_entry
window.del = delete_entry

# Bind buttons
@when("click", "#addBtn")
def on_add(e): add_entry()

@when("click", "#pdfBtn")
def on_pdf(e): generate_pdf()

# Initial render
render_all()