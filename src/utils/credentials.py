client_id = "Client_Id_d731ae830f8e0f30" # Adicione aqui sua CLIENT_ID da gerencianet
client_secret = "Client_Secret_b99dccf75c043fe2a4" # Adicione aqui sua CLIENT_SECRET da gerencianet
certificado = 'certificados/certificado-producao.pem'
sandbox = True

# CREDENCIAIS SE SEU CERTIFICADO FOR DE HOMOLOGACAO
client_id_homologacao = 'Client_Id_493944299db401abb4' # Adicione aqui sua CLIENT_ID da gerencianet
client_secret_homologacao = 'Client_Secret_22e044074c3c8'  # Adicione aqui sua CLIENT_SECRET da gerencianet
certificado_homologacao = 'certificados/certificado-homologacao.pem'

chave_pix = '65906cbf-abea-4fe1-ad2a-c0e1e719f36b' # COLOQUE SUA CHAVE PIX, CRIADA PELO APP DA GERENCIANET
       
# encoding: utf-8

# Put your app credentials here
CREDENTIALS = {
    'client_id': 'Client_Id_d731ae830f8e0', # Adicione aqui sua CLIENT_ID da gerencianet
    'client_secret': 'Client_Secret_b99dccf75', # Adicione aqui sua CLIENT_SECRET da gerencianet
    'sandbox': False,
    'pix_cert': 'certificados/certificado-producao.pem'
}

#openssl pkcs12 -in homologacao-379507-rifa-pix.p12 -out certificado.pem -nodes
