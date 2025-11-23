import solara

@solara.component
def Page():
    # 設定瀏覽器標籤頁的標題
    solara.Title("蔡婕妍的 Solara WebGIS App")
    solara.Markdown("### **花蓮馬太鞍溪堰塞湖 WebGIS 應用程式**")
    solara.image('https://row.github.com/Jie-Yan094/1119-Hualien/blob/8611836f4ef93b6cf959394c56ee8cac8cab78de/2.jpg')