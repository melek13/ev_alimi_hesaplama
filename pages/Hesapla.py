import streamlit as st

st.header("Hesaplama Sayfası")

with st.form("hesapla"):
    ev_fiyati = st.number_input("Alacağınız evin fiyatı ne kadar?")
    birikim_miktari = st.number_input("Ayda ne kadar biriktirebilirsiniz?")
    yas = st.number_input("Kaç yaşınızda biriktirmeye başlayacaksınız?")
    yasson = st.number_input("Kaç yaşınıza biriktirmeye devam edeceksiniz?")
    kira = st.number_input("Alacağınız evin kirası ne kadar?")
    evyuzde = st.number_input("Evinizin peşinatı ne kadar?(yüzdelik olarak yazınız (ör: %20 ise 0.20 olarak belirtin))") * ev_fiyati

    hesapla = st.form_submit_button("Hesapla")


    if hesapla:
            ay = 0
            ev_sayisi = 0
            toplam_birikim = 0
            toplam_odenen_borc = 0
            borc_sayac = 0
            kalan_ucret = 0


            while yas < yasson:
                ay += 1
                toplam_birikim += birikim_miktari

                if ay % 12 == 0:
                    yas += 1

                if toplam_birikim >= evyuzde:
                    ev_sayisi += 1
                    toplam_birikim -= evyuzde

                    st.write("Ay:", ay)
                    st.write("Ev Sayısı:", ev_sayisi)
                    st.write("Toplam birikim:", toplam_birikim)
                    st.write("Toplam kira:", kira * ev_sayisi)
                    st.write("Kalan ücret", kalan_ucret)

                toplam_birikim += (kira * ev_sayisi)


                kalan_ucret = int(ev_fiyati - evyuzde)
                kredi_tutari = int(kalan_ucret / 15)
                aylik_odeme = int(kredi_tutari / 12)

                toplam_birikim -= (aylik_odeme * ev_sayisi)
                toplam_odenen_borc += aylik_odeme * ev_sayisi
                borc_sayac += 1
                print("Borç sayaç", borc_sayac)

                if borc_sayac == 180:
                    borc_sayac -= 180
                    toplam_odenen_borc -= kalan_ucret
                    aylik_odeme -= (aylik_odeme * borc_sayac)


                if yas == yasson:
                    break

            st.write("*******************************")
            st.write("Toplam", ev_sayisi, "eviniz var.")
            st.write("Kiraların Toplamı:", kira * ev_sayisi)
            st.write("Geriye kalan borcunuz :", toplam_odenen_borc * (ev_sayisi * kalan_ucret))
            st.write("*******************************")



