# library
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title = 'Scatter SNBP NF')

image = Image.open('logo.png')

st.image(image)

st.header('Scatter Peminat vs Kuota SNBP')

# database
sheet_id = '1qNV58g5NE8iaaGbhpwPk0Ng2d8Si3lDsrkNLREQZ1xI'
snbp = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv')

kode_akses = st.text_input('Kode Akses', type='password')

if kode_akses == 'nfcemerlang':
	st.markdown('---')

	# sortir 
	# Pilihan Kampus
	ptn = pd.DataFrame({'kampus':['UNSYIAH', 'UNIMAL', 'UTU', 'UNSAM', 'UIN-AR-RANIRY', 'USU', 'UNIMED', 
			'UIN-SU', 'UNRI', 'UIN-SUSKA', 'UMRAH', 'UNAND', 'UNP', 'UNJA', 'UNIB', 'UNSRI', 
		    'UIN-RADENFATAH', 'UBB', 'UNILA', 'ITERA', 'UNTIRTA', 'UI', 'UIN-JKT', 'UNJ', 
		    'UPNVJ', 'UT', 'UNSIKA', 'ITB', 'UNPAD', 'UPI', 'UIN-SGD', 'IPB', 'UNSIL', 'UNSOED', 
		    'UNTIDAR', 'UNS', 'UNDIP', 'UNNES', 'UIN-WALISONGO', 'UNY', 'UPNYK', 'UIN-SUKA', 
		    'UNEJ', 'UB', 'UM', 'UIN-MALANG', 'UNAIR', 'ITS', 'UNESA', 'TRUNOJOYO', 'UPNJATIM', 
		    'UIN-SBY', 'UNTAN', 'UPR', 'ULM', 'UNMUL', 'ITK', 'UBT', 'UNUD', 'UNDIKSHA', 'UNRAM', 
		    'UNDANA', 'UNIMOR', 'UNHAS', 'UNM', 'UIN-ALAUDDIN', 'UNSRAT', 'UNIMA', 'UNTAD', 'UNSULBAR', 
		    'UHO', 'UNG', 'USN', 'UNPATTI', 'UNKHAIR', 'UNCEN', 'UNMUS', 'UNIPA', 'UGM']})	

	st.subheader('Pilihan Kampus dan Kelompok Prodi')
	kampus1 = st.multiselect('Pilih Kampus : ', options = ptn ['kampus'], default = ['UI', 'UNPAD', 'UNDIP', 'UGM'])

	if kampus1 == "":
		st.error('Silahkan input kampus')

	# fiter persis dengan apa yang ditulis
	filterKampus = snbp[snbp['ptn'].isin(kampus1)]

	kampus = pd.DataFrame({'kps':['ADMINISTRASI BISNIS','ARSITEKTUR','ASTRONOMI','BIOFISIKA','BIOLOGI',
			'BIOTEKNOLOGI, BIOKEWIRAUSAHAAN, BIOINFORMATIKA','BISNIS','DESAIN','EKONOMI','FILSAFAT','FISIKA',
			'GEOGRAFI, GEOGRAFI LINGKUNGAN, SAINS INFORMASI GEOGRAFIS','HUKUM','ILMU  ATAU SAINS VETERINER',
			'ILMU ATAU SAINS AKUNTANSI','ILMU ATAU SAINS GIZI','ILMU ATAU SAINS INFORMASI','ILMU ATAU SAINS KEBUMIAN',
			'ILMU ATAU SAINS KEDOKTERAN','ILMU ATAU SAINS KEDOKTERAN GIGI','ILMU ATAU SAINS KELAUTAN',
			'ILMU ATAU SAINS KEOLAHRAGAAN','ILMU ATAU SAINS KOMUNIKASI','ILMU ATAU SAINS LINGKUNGAN',
			'ILMU ATAU SAINS MANAJEMEN','ILMU ATAU SAINS MILITER','ILMU ATAU SAINS PERIKANAN',
			'ILMU DAN SAINS PERTANIAN','ILMU FARMASI','INFORMATIKA MEDIS ATAU INFORMATIKA KESEHATAN','KEBIDANAN',
			'KEHUTANAN','KEPERAWATAN','KESEHATAN','KESEHATAN MASYARAKAT','KIMIA','KOMPUTER',
			'KONSERVASI BIOLOGI, KONSERVASI HEWAN LIAR, KONSERVASI HEWAN LIAR, KONSERVASI HEWAN LIAR DAN HUTAN, KONSERVASI HUTAN, KONSERVASI SUMBER DAYA ALAM',
			'LINGUISTIK','LOGIKA','LOGISTIK','MATEMATIKA','PARIWISATA','PERENCANAAN WILAYAH','PERTAHANAN','PETERNAKAN',
			'PSIKOLOGI','SAINS DATA','SAINS PERKOPIAN','SEJARAH','SENI','SOSIAL','STUDI  HUMANITAS','SUSASTRA ATAU SASTRA',
			'TEKNIK ATAU REKAYASA','TEKNOLOGI PANGAN, TEKNOLOGI HASIL PERTANIAN / PETERNAKAN / PERIKANAN','TRANSPORTASI',
			'URUSAN PUBLIK']})

	# Pilihan Kps
	kps1 = st.multiselect('Pilih Kelompok Program Studi : ', options = kampus ['kps'], default = ['SUSASTRA ATAU SASTRA'])

	if kps1 == "":
		st.error('Silahkan input kampus')

	# fiter persis dengan apa yang ditulis
	filterKps = filterKampus[filterKampus['kelompok_program_studi'].isin(kps1)]



	# Scatter peminat dan daya tampung
	x_values = filterKps['peminat']
	y_values = filterKps['daya_tampung']
	n = filterKps['prodi']
	o = filterKps['ptn']
	plot = px.scatter(data_frame = filterKps, x=x_values, y=y_values, size=y_values, color=n, hover_data=[o])
	st.plotly_chart(plot)
