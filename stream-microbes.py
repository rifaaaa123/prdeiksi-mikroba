import pickle
import streamlit as st

# membaca model
microbes_model =  pickle.load(open('mikroba_model.sav', 'rb'))

#Judul Web
st.title('Data Mining Prediksi Jenis Mikroba')

Solidirity = st.text_input('Masukan Ratio Solidirity')

Eccentricity = st.text_input('Masukan Ratio Accentricity')

EquivDiameter = st.text_input('Masukan Diameter Lingkaran')

Extrema = st.text_input('Masukan Titik Ekstrem')

FilledArea = st.text_input('Masukan Jumlah Piksel')

Extent = st.text_input('Masukan Rasio Extent')

Orientation = st.text_input('Masukan Overall Orientation')

EulerNumber = st.text_input('Masukan Number Euler')

BoundingBox1 = st.text_input('Masukan Kotak Pembatas 1')

BoundingBox2 = st.text_input('Masukan Kotak Pembatas 2')

BoundingBox3 = st.text_input('Masukan Kotak Pembatas 3')

BoundingBox4 = st.text_input('Masukan Kotak Pembatas 4')

ConvexHull1 = st.text_input('Masukan Lambung Cembung 1')

ConvexHull2 = st.text_input('Masukan Lambung Cembung 2')

ConvexHull3 = st.text_input('Masukan Lambung Cembung 3')

ConvexHull4 = st.text_input('Masukan Lambung Cembung 4')

MajorAxisLength = st.text_input('Masukan Panjang Sumbu Utama')

MinorAxisLength = st.text_input('Masukan Panjang Sumbu Minor')

Perimeter = st.text_input('Masukan Nilai Meteran')

ConvexArea = st.text_input('Masukan Nilai Area Cembung')

Centroid1 = st.text_input('Masukan Nilai Sentroid 1')

Centroid2 = st.text_input('Masukan Nilai Sentroid 2')

Area = st.text_input('Masukan Atribut Area')

raddi = st.text_input('Masukan Atribut Raddi')

# code untuk kelompok jenis mikroba
microbes_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi'):
    microbes_prediction = microbes_model.predict([[Solidirity, Eccentricity, EquivDiameter, Extrema, FilledArea, Extent, Orientation, EulerNumber, BoundingBox1, BoundingBox2, BoundingBox3, BoundingBox4, ConvexHull1, ConvexHull2, ConvexHull3, ConvexHull4, MajorAxisLength, MinorAxisLength, Perimeter, ConvexArea, Centroid1, Centroid2, Area, raddi]])
    
    if(microbes_prediction[0] == 0):
        microbes_diagnosis = 'Jenis Mikroba Spirogyra'
    else :
        microbes_diagnosis = 'Jenis Mikroba Volvox'

    st.success(microbes_diagnosis)