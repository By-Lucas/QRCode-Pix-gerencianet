client_id = "Client_Id_d731ae830f8e0f308603fffea3a8a748436e946a"
client_secret = "Client_Secret_b99dccf75c043fe2a47518dc02561d8d9b032aef"
certificado = 'certificados/certificado-producao.pem'
sandbox = True

# CREDENCIAIS HOMOLOGACAO
client_id_homologacao = 'Client_Id_493944299db401abb42a0251b0e28cf0eda2a507'
client_secret_homologacao = 'Client_Secret_22e044074c3c82f4bf95400756f323ed7608907c'
certificado_homologacao = 'certificados/certificado-homologacao.pem'

chave_pix = '65906cbf-abea-4fe1-ad2a-c0e1e719f36b'
       
# encoding: utf-8

# Put your app credentials here
CREDENTIALS = {
    'client_id': 'Client_Id_d731ae830f8e0f308603fffea3a8a748436e946a',
    'client_secret': 'Client_Secret_b99dccf75c043fe2a47518dc02561d8d9b032aef',
    'sandbox': False,
    'pix_cert': 'certificados/certificado-producao.pem'
}

#openssl pkcs12 -in homologacao-379507-rifa-pix.p12 -out certificado.pem -nodes