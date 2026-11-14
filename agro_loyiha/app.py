import streamlit as st

# Sahifa sozlamalari
st.set_page_config(page_title="Agro-Almashinuv AI", layout="centered")

# Sarlavha va tavsif
st.title("Aqlli Ekin Almashinuvi Strategiyasi")
st.write("Fermerlar uchun tuproq unumdorligini oshirish va suv resurslarini tejashga asoslangan tavsiya tizimi.")
st.divider()

# 1. Ma'lumotlarni kiritish qismi
st.subheader("1. Maydon ma'lumotlarini kiriting")

col1, col2 = st.columns(2)

with col1:
    hudud = st.selectbox(
        "Hududni tanlang:",
        ["Qashqadaryo", "Samarqand", "Buxoro", "Farg'ona", "Surxondaryo", "Toshkent", "Xorazm"]
    )
    oldingi_ekin = st.selectbox(
        "O'tgan mavsumda ekilgan ekin:",
        ["Paxta", "Bug'doy", "Makkajo'xori", "Sabzavotlar (Pomidor, Kartoshka)", "Poliz ekinlari"]
    )

with col2:
    suv_holati = st.radio(
        "Suv ta'minoti holati:",
        ["Yetarli", "O'rtacha", "Tanqis"]
    )
    shorlanish = st.select_slider(
        "Tuproq sho'rlanish darajasi:",
        options=["Past", "O'rtacha", "Yuqori"]
    )

maydon_gektar = st.number_input("Yer maydoni (gektar hisobida):", min_value=1.0, max_value=1000.0, value=10.0, step=1.0)

st.divider()

# 2. Tahlil va tavsiya berish qismi
if st.button("Eng maqbul strategiyani aniqlash", type="primary"):
    st.subheader("2. Tavsiya etiladigan ekin almashinuvi strategiyasi")
    
    asosiy_ekin = ""
    takroriy_ekin = ""
    sabab = ""
    suv_tejash = 0
    azot_foydasi = ""

    # Agronomik mantiq
    if oldingi_ekin == "Paxta":
        if suv_holati == "Tanqis" or shorlanish == "Yuqori":
            asosiy_ekin = "Beda yoki Arpa"
            takroriy_ekin = "Talab etilmaydi (ko'p yillik yoki kuzgi)"
            sabab = "Paxtadan keyin charchagan va sho'rlangan tuproqni tiklaydi. Beda ildizlari tuproq strukturasini yumshatadi va sho'rni kamaytiradi."
            suv_tejash = 35
            azot_foydasi = "Yuqori (Gektariga 150-200 kg tabiiy azot to'playdi)"
        else:
            asosiy_ekin = "Kuzgi bug'doy"
            takroriy_ekin = "Mosh yoki Soya"
            sabab = "G'alla tuproqdagi paxta kasalliklarini yo'qotadi. Yozda ekilgan mosh esa tuproqni tabiiy azot bilan boyitadi."
            suv_tejash = 20
            azot_foydasi = "O'rtacha (Takroriy dukkakli ekin hisobiga)"

    elif oldingi_ekin == "Bug'doy":
        if suv_holati == "Tanqis":
            asosiy_ekin = "No'xat yoki Loviya"
            takroriy_ekin = "Kungaboqar (ertapishar)"
            sabab = "Dukkakli ekinlar kam suv talab qiladi va g'alladan keyin bo'shagan yerning unumdorligini tez tiklaydi."
            suv_tejash = 40
            azot_foydasi = "Yuqori (Tuproq unumdorligini 25% ga oshiradi)"
        else:
            asosiy_ekin = "Makkajo'xori (don yoki silos uchun)"
            takroriy_ekin = "Kuzgi sabzavotlar"
            sabab = "Suv yetarli bo'lgan sharoitda yuqori daromad va chorva uchun ozuqa bazasini yaratadi."
            suv_tejash = 10
            azot_foydasi = "Past (Qo'shimcha mineral o'g'it talab qiladi)"

    elif oldingi_ekin == "Makkajo'xori":
        asosiy_ekin = "Soya yoki Mosh"
        takroriy_ekin = "Kuzgi raps (yashil o'g'it sifatida)"
        sabab = "Makkajo'xori tuproqdan ko'p ozuqa oladi. Soya esa uni qayta tiklab, keyingi yilgi hosilga zamin yaratadi."
        suv_tejash = 30
        azot_foydasi = "Juda yuqori"

    else:
        asosiy_ekin = "Kuzgi bug'doy yoki Arpa"
        takroriy_ekin = "Beda"
        sabab = "Sabzavot va poliz ekinlaridan keyin begona o'tlar ko'payadi. Boshoqli ekinlar yerni tozalashga yordam beradi."
        suv_tejash = 25
        azot_foydasi = "O'rtacha"

    # Natijalarni chiroyli kartochkalarda chiqarish
    st.success(f"**Asosiy tavsiya etiladigan ekin:** {asosiy_ekin}")
    st.info(f"**Takroriy ekin (2-hosil):** {takroriy_ekin}")
    
    st.write(f"**Ilmiy asos:** {sabab}")

    # Ko'rsatkichlar (Metrikalar)
    m1, m2, m3 = st.columns(3)
    m1.metric("Suv tejamkorligi", f"{suv_tejash}%", "An'anaviy usulga nisbatan")
    m2.metric("Umumiy maydon", f"{maydon_gektar} ga", hudud)
    m3.metric("Tuproqqa azot foydasi", azot_foydasi.split(" ")[0])

    st.caption(f"Batafsil: {azot_foydasi}")
