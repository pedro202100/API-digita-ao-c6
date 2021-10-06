from os import replace, times
from types import TracebackType
from flask import Flask, json, render_template
from flask import request
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common import by, keys
from selenium.webdriver.remote.utils import dump_json
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import TimeoutException
from datetime import datetime
from datetime import timedelta
from flask import jsonify
from json import dumps


app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def pega_dados():
    
    request_data = request.get_json()
    
    if request_data:
        ################################ ACESSO
        if 'acesso' in request_data:
            senha1 = request_data['acesso']
            global senha
            senha = senha1['senha']

            usuario1 = request_data['acesso']
            global usuario
            usuario = usuario1['usuario']          
        ############################### Dados cadastrais
        if 'dadosCadastrais' in request_data:
            dadosCadastrais = request_data['dadosCadastrais']
            ########### CPF #
            global cpf
            cpf = dadosCadastrais['cpf']
            ############# data_doc #
            global data_doc
            datadoc5 = dadosCadastrais ['dataEmissaoDocumento']
            datadoc = datadoc5.split('-')
            datadoc2 = datadoc[2]
            datadoc3 = datadoc[1]
            datadoc4 = datadoc[0]
            data_doc = datadoc2+'/'+datadoc3+'/'+datadoc4
            ############# data_nasci #
            global data_nasci
            data5 = dadosCadastrais ['dataNascimento']
            data1 = data5.split('-')
            data2 = data1[2]
            data3 = data1[1]
            data4 = data1[0]
            data_nasci = data2+'/'+data3+'/'+data4
            
            ############# dataRenda #
            global dataRenda
            data6 = dadosCadastrais ['dataRenda']
            data7 = data5.split('-')
            data8 = data1[2]
            data9 = data1[1]
            data10 = data1[0]
            dataRenda = data8+'/'+data9+'/'+data10    

            ############# especie #
            global especie
            especie = dadosCadastrais ['especie']
            ############# fluxo
            global fluxoIN100
            fluxoIN100 = dadosCadastrais['fluxoIN100']
            ############ tempoResidencia
            tempoResidencia = dadosCadastrais['tempoResidencia']
            ############## descontosCompulsorios
            global descontosCompulsorios
            descontosCompulsorios = dadosCadastrais['descontosCompulsorios']
            ############## descontosVariaveis
            global descontosVariaveis
            descontosVariaveis = dadosCadastrais['descontosVariaveis']
            ############## valorParcelasOutrosBancos
            valorParcelasOutrosBancos = dadosCadastrais['valorParcelasOutrosBancos']
            ############## email
            email = dadosCadastrais['email']
            ############# matricula #
            global matricula
            matricula = dadosCadastrais ['matricula']
            ############# valorRenda #
            global valorRenda
            valorRenda = dadosCadastrais ['valorRenda']
            ############# ufContaBeneficio #
            global ufContaBeneficio
            ufContaBeneficio = dadosCadastrais ['ufContaBeneficio']
            ############# nome #
            global nome
            nome = dadosCadastrais ['nome']
            ############# grauInstrucao #
            global grauInstrucao
            grauInstrucao = dadosCadastrais ['grauInstrucao']
            ############# sexo 
            global sexo 
            sexo = dadosCadastrais['sexo']
            ############# estadoCivil #
            global estadoCivil
            estadoCivil = dadosCadastrais ['estadoCivil']
            ############# mae #
            global mae
            mae = dadosCadastrais ['mae']           
            ############# pai #
            global pai
            pai = dadosCadastrais ['pai']
            ############# conjuge #
            global conjuge
            conjuge = dadosCadastrais ['conjuge']
            ############# naturalidade #
            global naturalidade
            naturalidade = dadosCadastrais ['naturalidade']
            ############# ufNaturalidade #
            global ufNaturalidade
            ufNaturalidade = dadosCadastrais ['ufNaturalidade']
            ############# nacionalidade #
            global nacionalidade
            nacionalidade = dadosCadastrais ['nacionalidade']
             ############# tipoDocumento #
            global tipoDocumento
            tipoDocumento = dadosCadastrais ['tipoDocumento']
            ############# documento #
            global documento
            documento = dadosCadastrais ['documento']
            ############# orgaoEmissor #
            global orgaoEmissor
            orgaoEmissor = dadosCadastrais ['orgaoEmissor']
            ############# ufDocumento #
            global ufDocumento
            ufDocumento = dadosCadastrais ['ufDocumento']

        if 'dadosCadastrais' in request_data:

            endereco1 = request_data['dadosCadastrais']
            endereco = endereco1['endereco']
            ########### CPF #
            global cep
            cep = endereco['cep']
            ########### CPF #
            global logradouro
            logradouro = endereco['logradouro']
            ########### CPF #
            global numero
            numero = endereco['numero']
            ########### complemento
            global complemento
            complemento = endereco['complemento']
            ########### CPF #
            global ufEndereco
            ufEndereco = endereco['ufEndereco']
            ########### CPF #
            global municipio
            municipio = endereco['municipio']
            ########### CPF #
            global bairro
            bairro = endereco['bairro']
        
        if 'dadosCadastrais' in request_data:
            tipo_telefone = request_data['dadosCadastrais']
            telefone = tipo_telefone['telefones']
            global telefone_principal
            telefone_principal = telefone[1]
            global ddd_tel
            ddd_tel = telefone_principal['ddd']
            global numero_tel
            numero_tel = telefone_principal['telefone']
        
        if 'dadosCadastrais' in request_data:
            banco2 = request_data['dadosCadastrais'] 
            ######## BANCO
            global banco
            banco = banco2['banco']
            ######### AGENCIA
            global agencia
            agencia = banco2['agencia']
            ######### Digito AG
            global digito
            digito = banco2["digitoAgencia"]
            ######### CONTA
            global conta 
            conta = banco2['conta']
            ######### digitoConta
            global digitoConta
            digitoConta = banco2['digitoConta']
            ######## tipoConta
            global tipoConta
            tipoConta = banco2['tipoConta'] ##CONTA_MOVTO
            
        if 'dadosProposta' in request_data:

            dadosProposta = request_data['dadosProposta']
            ###### convenio
            global convenio
            convenio = dadosProposta['convenio']
            ###### cpfAgente
            global cpfAgente
            cpfAgente = dadosProposta['cpfAgente']
            ###### carencia
            global carencia 
            carencia = dadosProposta['carencia']
            ###### formaLiberacao
            global formaLiberacao
            formaLiberacao = dadosProposta['formaLiberacao']
            ###### valorSolicitado
            global valorSolicitado
            valorSolicitado = dadosProposta['valorSolicitado']
            ###### quantidadeParcelas
            global quantidadeParcelas 
            quantidadeParcelas = dadosProposta['quantidadeParcelas']
            ###### valorParcela
            global valorParcela
            valorParcela = dadosProposta['valorParcela']   

def matri():
    matri = int(matricula)
    return matri

def parcela():
    parcela1 = str(valorParcela)
    parcela = parcela1.replace(".",",")
    return parcela

def ufcidade(local):
    uf = local
    if uf == 'SAO_PAULO':
        uf = 'SP'
        return uf
    elif uf == 'ACRE':
        uf = 'AC'
        return uf
    elif uf == 'AMAPA':
        uf = 'AP'
        return uf
    elif uf == 'ALAGOAS':
        uf = 'AL'
        return uf    
    elif uf == 'AMAZONAS':
        uf = 'AM'
        return uf   
    elif uf == 'BAHIA':
        uf = 'BA'
        return uf   
    elif uf == 'CEARA':
        uf = 'CE'
        return uf
    elif uf == 'DISTRITO_FEDERAL':
        uf = 'DF'
        return uf       
    elif uf == 'ESPIRITO_SANTO':
        uf = 'ES'
        return uf    
    elif uf == 'GOIAS':
        uf = 'GO'
        return uf
    elif uf == 'MARANHAO':
        uf = 'MA'
        return uf    
    elif uf == 'MATO_GROSSO':
        uf = 'MT'
        return uf   
    elif uf == 'MATO_GROSSO_DO_SUL':
        uf = 'MS'
        return uf    
    elif uf == 'MINAS_GERAIS':
        uf = 'MG'
        return uf   
    elif uf == 'PARA':
        uf = 'PA'
        return uf        
    elif uf == 'PARAIBA':
        uf = 'PB'
        return uf
    elif uf == 'PARANA':
        uf = 'PR'
        return uf    
    elif uf == 'PERNAMBUCO':
        uf = 'PE'
        return uf
    elif uf == 'PIAUI':
        uf = 'PI'
        return uf
    elif uf == 'RIO_DE_JANEIRO':
        uf = 'RJ'
        return uf
    elif uf == 'RIO_GRANDE_DO_NORTE':
        uf = 'RN'
        return uf
    elif uf == 'RIO_GRANDE_DO_SUL':
        uf = 'RS'
        return uf    
    elif uf == 'RONDONIA':
        uf = 'RO'
        return uf    
    elif uf == 'RORAIMA':
        uf = 'RR'
        return uf   
    elif uf == 'SANTA_CATARINA':
        uf = 'SC'
        return uf    
    elif uf == 'SERGIPE':
        uf = 'SE'
        return uf    
    elif uf == 'TOCANTINS':
        uf = 'TO'
        return uf    
    else:
        print('estado nao indentificado')

def ufDoc():
    ufcidade(ufDocumento)

global text_uf
text_uf = None

def text_uf1():
    ufcidade(ufEndereco)
    

def doc_uf():
    ufcidade(ufEndereco)

def uf_natural():
    ufcidade(ufNaturalidade)

def valor_renda():
    valor_renda = str(valorRenda)
    valor_renda1 =valor_renda.replace('.',',')
    return valor_renda1

global opcao1
opcao1 = None

def carencia1():

   if carencia == '000197':
        opcao1 = '5'
   return opcao1

@app.route('/digitacao/', methods=['POST','GET'])

def digitacao():

    pega_dados()

    opcao = carencia1()
    
    navegadorBanco = webdriver.Chrome()
    navegadorBanco.get('https://c6.c6consig.com.br/WebAutorizador/Login/AC.UI.LOGIN.aspx?FISession=5436fe50aea6')
    
    def espera_alerta():
        try:
            WebDriverWait(navegadorBanco, 4).until(EC.alert_is_present())
            alert = navegadorBanco.switch_to.alert
            alert.accept()
            print("alert accepted")
        except TimeoutException:
            print("no alert")

    while len(navegadorBanco.find_elements_by_id('EUsuario_CAMPO')) <= 0:
        time.sleep(1)

    time.sleep(2)

    navegadorBanco.find_element_by_id('EUsuario_CAMPO').send_keys(usuario)
    time.sleep(1)
    navegadorBanco.find_element_by_id('ESenha_CAMPO').send_keys(senha)
    time.sleep(1)
    navegadorBanco.find_element_by_xpath('//*[@id="lnkEntrar"]').click()

    try:
        WebDriverWait(navegadorBanco, 3).until(EC.alert_is_present())
        alert = navegadorBanco.switch_to.alert 
        alert.accept()
        print("alert accepted")
    except TimeoutException:
        print("no alert")

    time.sleep(1)

        
    while len(navegadorBanco.find_elements_by_id('content')) <= 0:
        time.sleep(1)

    

    navegadorBanco.get(navegadorBanco.find_element_by_id('WFP2010_PWCDPRPS').get_attribute("href"))
    time.sleep(6)

    

    while len(
            navegadorBanco.find_elements_by_id('ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_cboTipoOperacao_CAMPO')) <= 0:
        time.sleep(1)
    navegadorBanco.find_element_by_css_selector(
        "#ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_cboTipoOperacao_CAMPO [value='MargemLivre']").click()
    time.sleep(2)

    antes = datetime.today()

    while len(navegadorBanco.find_elements_by_css_selector(
        "#ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_cboGrupoConvenio_CAMPO [value='5']")) <= 0:
        time.sleep(1)
    navegadorBanco.find_element_by_css_selector(
    "#ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_cboGrupoConvenio_CAMPO [value='5']").click()
    time.sleep(1)

    navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_rblTpFormalizacao_1').click()
    time.sleep(1)

    navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_txtCPF_CAMPO').send_keys(cpf)
    navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_txtCPF_CAMPO').send_keys(Keys.TAB)

    time.sleep(5)

    element2 = navegadorBanco.find_element_by_css_selector('#ctl00_UpdPrs')
    while element2.value_of_css_property('display') != 'none':
            time.sleep(1)   

    if len(navegadorBanco.find_elements_by_id('ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_popCliente_frameAjuda')) > 0:
        
        navegadorBanco.switch_to.default_content()
        # Pega o XPath do iframe e atribui a uma variável
        iframe = navegadorBanco.find_element_by_xpath(
        '//*[@id="ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_popCliente_frameAjuda"]')

        # Muda o foco para o iframe
        navegadorBanco.switch_to.frame(iframe)

        navegadorBanco.find_element_by_xpath('//*[@id="ctl00_cph_FIJanela1_FIJanelaPanel1_btnNovo_dvTxt"]/table/tbody/tr/td').click()

        # Retorna para a janela principal (fora do iframe)
        navegadorBanco.switch_to.default_content()
        
        time.sleep(0.5)
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_txtDataNascimento_CAMPO').send_keys(
            data_nasci)
        time.sleep(0.5)
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_txtDataNascimento_CAMPO').send_keys(
            Keys.TAB)
        time.sleep(2)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_ucMatricula_txtMatricula_CAMPO').send_keys(matricula)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_ucMatricula_txtMatricula_CAMPO').send_keys(Keys.TAB)

        element2 = navegadorBanco.find_element_by_css_selector('#ctl00_UpdPrs')
        while element2.value_of_css_property('display') != 'none':
            time.sleep(1)
            
        time.sleep(6)
    
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_txtRenda_CAMPO').clear()
        time.sleep(2)
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_txtRenda_CAMPO').send_keys(valor_renda())
        time.sleep(0.6)
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_txtRenda_CAMPO').send_keys(Keys.TAB)
        time.sleep(2)

        today = datetime.today()
        first = today.replace(day=1)
        lastMonth = first - timedelta(days=1)
        month = lastMonth.strftime("%m")
        years = lastMonth.strftime("%Y")

        monthLast = month+'/'+years
        monthLast1 = str(monthLast)

        print(monthLast1)

        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_txtDataContraCheque_CAMPO').send_keys(monthLast1)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_txtDataContraCheque_CAMPO').send_keys(Keys.TAB)
        time.sleep(2)

        navegadorBanco.find_element_by_id('btnObterMargem_txt').click()

        time.sleep(3)

        
        
        try:
            WebDriverWait(navegadorBanco, 10).until(EC.alert_is_present())
            alert = navegadorBanco.switch_to.alert
            alert.accept()
            print("alert accepted")
        except TimeoutException:
            print("no alert") 
            
        #################################################   CAMPO DADOS PESSOAIS

        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtNome_CAMPO').clear()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtNome_CAMPO').send_keys(nome)
        time.sleep(2)

        if (nacionalidade == 'BRASILEIRA') or (nacionalidade == 'BRASILEIRO'):
            print('true')
        else:
            navegadorBanco.find_element_by_xpath(
                '//*[@id="ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_cbxNacionalidade_CAMPO"]/option[2]').click()
        time.sleep(1)
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtNatural_CAMPO').clear()
        time.sleep(1)
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtNatural_CAMPO').send_keys(naturalidade)

        time.sleep(1.5)

        if sexo == 'FEMININO':
            navegadorBanco.find_element_by_xpath(
                '//*[@id="ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_cbxSexo_CAMPO"]/option[3]').click()
        else:
            navegadorBanco.find_element_by_xpath(
                '//*[@id="ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_cbxSexo_CAMPO"]/option[2]').click()

        time.sleep(0.5)

        if estadoCivil == 'SOLTEIRO':
            navegadorBanco.find_element_by_css_selector(
            "#ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_cbxEstadoCivil_CAMPO > option:nth-child(2)").click()   
        elif estadoCivil == 'CASADO':
             navegadorBanco.find_element_by_css_selector(
                 '#ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_cbxEstadoCivil_CAMPO > option:nth-child(3)').click()
        elif estadoCivil == 'DESQUITADO':
            navegadorBanco.find_element_by_css_selector(
                '#ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_cbxEstadoCivil_CAMPO > option:nth-child(4)').click()
        elif estadoCivil == 'DIVORCIADO':
            navegadorBanco.find_element_by_css_selector(
                '#ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_cbxEstadoCivil_CAMPO > option:nth-child(5)').click()
        elif estadoCivil == 'VIUVO':
            navegadorBanco.find_element_by_css_selector(
                '#ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_cbxEstadoCivil_CAMPO > option:nth-child(6)').click()
        elif estadoCivil == 'OUTROS':        
            navegadorBanco.find_element_by_css_selector(
                '#ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_cbxEstadoCivil_CAMPO > option:nth-child(7)').click()
        else:
            print('nao escolhido')

        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtDocumento_CAMPO').clear()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtDocumento_CAMPO').send_keys(documento)

        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtEmissor_CAMPO').clear()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtEmissor_CAMPO').send_keys(orgaoEmissor)
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtDataEmissao_CAMPO').clear()
        time.sleep(0.5)
        navegadorBanco.find_element_by_css_selector(
            "#ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_cbxUFDoc_CAMPO [value='" + doc_uf() + "']").click()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtDataEmissao_CAMPO').send_keys(
            data_doc)
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtMae_CAMPO').clear()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtMae_CAMPO').send_keys(mae)
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtDddTelCelular_CAMPO').clear()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtDddTelCelular_CAMPO').send_keys(
            ddd_tel)
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtTelCelular_CAMPO').clear()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtTelCelular_CAMPO').send_keys(
            numero_tel)
        time.sleep(0.5)
        ############################################## DADOS DO ENDEREÇO
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnCR_txtNumero_CAMPO').clear()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnCR_txtCEP_CAMPO').clear()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnCR_txtCEP_CAMPO').send_keys(cep)
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnCR_txtCEP_CAMPO').send_keys(Keys.TAB)
        
        time.sleep(2.5)

        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnCR_txtEndereco_CAMPO').send_keys(
            logradouro)
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnCR_txtNumero_CAMPO').send_keys(
            numero)
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnCR_txtBairro_CAMPO').send_keys(
            bairro)
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnCR_txtCidade_CAMPO').send_keys(
            municipio)
        time.sleep(0.5)
        navegadorBanco.find_element_by_css_selector(
            "#ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_cbxUFBeneficio_CAMPO [value='" + uf_natural() + "']").click()
        time.sleep(0.5)
        ########################################## DADOS DA SIMULAÇAO
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_txtVlrParcela_CAMPO').clear()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_txtVlrParcela_CAMPO').send_keys(
            parcela())
        time.sleep(1)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_UcBtnCalc_btnCalcular_dvCBtn').click()
        time.sleep(5)

        element2 = navegadorBanco.find_element_by_css_selector('#ctl00_UpdPrs')
        while element2.value_of_css_property('display') != 'none':
            time.sleep(1)

        ########################################### CONDIÇOES ESCOLHIDAS

        if len(navegadorBanco.find_elements_by_id('ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_grdCondicoes_ctl02_lblObs')) >= 1:
            final1 = datetime.today()
            final = str(final1)
            fim = (final1 - antes)

            navegadorBanco.quit()

            return dumps({ 
                "status":"FORBIDDEN",
                "code":"403",
                "message":"Erro na digitaçao",
                "resultInfo":{
                    "timestamp": str(final),
                    "queryTime":str(fim),
                    "requestId":"e86c6b2ffb60e22c"
            },  
            })


           


        else:
            pass

        if opcao == '1':
            navegadorBanco.find_element_by_id(
                'ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_grdCondicoes_ctl02_ckSelecao').click()
        elif opcao == '2':
            navegadorBanco.find_element_by_id(
                'ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_grdCondicoes_ctl03_ckSelecao').click()
        elif opcao == '3':
            navegadorBanco.find_element_by_id(
                'ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_grdCondicoes_ctl04_ckSelecao').click()
        elif opcao == '4':
            navegadorBanco.find_element_by_id(
                'ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_grdCondicoes_ctl05_ckSelecao').click()
        elif opcao == '5':
            navegadorBanco.find_element_by_id(
                'ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_grdCondicoes_ctl06_ckSelecao').click()
        else:
            pyautogui.alert('erro na hora da seleçao de tabela, navegador sera fechado!')
            navegadorBanco.quit()
            
        ######################################## DADOS DA AVERBAÇAO
        time.sleep(3)
        data_venc = navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_UcGridFin_grdFinanciamento_ctl02_Label1').text
        time.sleep(0.5)
        valo_cli = navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_UcGridFin_grdFinanciamento_ctl03_Label1').text
        time.sleep(0.5)
        proposta = ''
        valor_Parcela = navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_UcGridFin_grdFinanciamento_ctl04_Label1').text
        time.sleep(0.5)
        valorFinanciado = navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_UcGridFin_grdFinanciamento_ctl05_Label1').text
        time.sleep(0.5)
        valorBruto = navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_UcGridFin_grdFinanciamento_ctl06_Label1').text
        time.sleep(0.5)
        quantidade_Parcelas = navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_UcGridFin_grdFinanciamento_ctl07_Label1').text
        
        if quantidade_Parcelas == '084':
            quantidade_Parcelas ='84'
        
        time.sleep(0.5)
        taxaCLAM1 = navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_UcGridFin_grdFinanciamento_ctl08_Label1').text
        taxaCLAM2 = str(taxaCLAM1).replace(',','.')
        taxaCLAM = taxaCLAM2[:4]
        time.sleep(0.5)
        taxaCETAM1 = navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_UcGridFin_grdFinanciamento_ctl09_Label1').text
        taxaCETAM = str(taxaCETAM1).replace(',','.')
        
        time.sleep(0.5)
        taxaCETLAA1 = navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_UcGridFin_grdFinanciamento_ctl10_Label1').text
        taxaCETLAA = str(taxaCETLAA1).replace(',','.')

        time.sleep(2)

        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_txtBeneficio_CAMPO').clear()
        time.sleep(2)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_txtBeneficio_CAMPO').send_keys(especie)
        time.sleep(2)
        navegadorBanco.find_element_by_css_selector(
            "#ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_cbxUFBeneficio_CAMPO [value='" + text_uf1() + "']").click()
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtBanco_CAMPO').clear()
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtAgencia_CAMPO').clear()
        time.sleep(2)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtBanco_CAMPO').send_keys(banco)
        navegadorBanco.find_element_by_id(
            "ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtBanco_CAMPO").send_keys(
            Keys.TAB)
        
        ###################################### COLO A AGENCIA DO BANCO ############################
        
        time.sleep(4)
        navegadorBanco.find_element_by_id(
            "ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtAgencia_CAMPO").send_keys(
            agencia)
        navegadorBanco.find_element_by_id(
            "ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtAgencia_CAMPO").send_keys(
            Keys.TAB)
        time.sleep(3)
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtDvAgencia_CAMPO').send_keys('0')
        time.sleep(4)

        ################################################# CONTA ###############
        ################################################# CONTA ###############
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtConta_CAMPO').click()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtConta_CAMPO').send_keys(conta)
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            "ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtConta_CAMPO").send_keys(
            Keys.TAB)
        ########################################## DIGITO CONTA
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtDvConta_CAMPO').send_keys(
            digitoConta)
        navegadorBanco.find_element_by_id(
            "ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtDvConta_CAMPO").send_keys(
            Keys.TAB)

        time.sleep(3)
    
        if formaLiberacao == 'TED_CONTA_CORRENTE':
            pass
        elif formaLiberacao == 'TED_CONTA_POUPANCA' :
                print('certo ')
                navegadorBanco.find_element_by_css_selector(
                    "#ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_FIJanelaPanel2_UcDadosPagamento_cbxTipoConta_CAMPO > option:nth-child(2)").click()
        else:
            alert('erro na parte de forma de liberaçao')
            
        ############################################# DIGITA O CPF DO AGENTE #########################

        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_FIJanelaPanel3_txtCpfOrigem3o_CAMPO').send_keys(cpfAgente) 
        print('antes')
        time.sleep(4)
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_FIJanelaPanel3_cbxOrigem6_CAMPO_EDIT').click()
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_FIJanelaPanel3_cbxOrigem6_CAMPO_EDIT').send_keys(Keys.TAB)
        time.sleep(3)
        navegadorBanco.find_element_by_id('btnGravar_txt').click()
        time.sleep(5)
        try:
            WebDriverWait(navegadorBanco, 30).until(EC.alert_is_present())
            time.sleep(0.5)
            texto = alert.text  
            time.sleep(0.5)              
            proposta1 = texto.split(' ')
            time.sleep(0.5)
            proposta = str(proposta1[6])
            time.sleep(0.5)
            alert.accept()

        except TimeoutException:
            print("no alert") 
        final1 = datetime.today()
        final = str(final1)
        
        fim = (final1 - antes)

        navegadorBanco.quit()

        return dumps({ 
            "proposta": str(proposta),
            "dataVencimento": str(data_venc),
            "valorCliente": str(valo_cli),
            "valorParcela": str(valor_Parcela),
            "valorFinanciado": str(valorFinanciado),
            "valorBruto": str(valorBruto),
            "quantidadeParcelas": str(quantidade_Parcelas),
            "taxaCLAM": str(taxaCLAM),
            "taxaCETAM": str(taxaCETAM),
            "taxaCETLAA": str(taxaCETLAA),
            "resultInfo":{
                "timestamp": str(final),
                "queryTime":str(fim),
                "requestId":"e86c6b2ffb60e22c"
        },
            "billingInfo":{
                  "value":"0.4",
                  "charged":'true',
                  "balance":'394.8',
                  "balanceValidUntil":"2021-08-17T00:00:00.000-0300",
                  "subscriptionId":"168gcbc85izyc"
                      } 
        })
            
        

        

        

        #return 'RETORNO:\n\nproposta: {}\n\ndata_venc: {}\n\nvalo_cli: {}\n\nvalor_Parcela: {}\n\nvalorFinanciado: {}\n\nvalorBruto: {}\n\nquantidade_Parcelas: {}\n\ntaxaCLAM: {}\n\ntaxaCETAM: {}\n\ntaxaCETLAA: {}\n\nresultInfo:\n\ntimestamp: {}\n\nqueryTime: {}\n\nrequestId: {}\n\nbillingInfo:\n\nvalue: {}\n\ncharged: {}\n\nbalance: {}\n\nbalanceValidUntil: {}\n\nsubscriptionId: {}'.format(proposta,data_venc,valo_cli,valor_Parcela,valorFinanciado, valorBruto, quantidade_Parcelas, taxaCLAM, taxaCETAM, taxaCETLAA,final,fim,'e86c6b2ffb60e22c','0.4','true','394.8','2021-08-17T00:00:00.000-0300','168gcbc85izyc')
        #########################################  ALERTA FIM  ##############################################
    else:

        time.sleep(0.5)
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_txtDataNascimento_CAMPO').send_keys(
            data_nasci)
        time.sleep(0.5)
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_txtDataNascimento_CAMPO').send_keys(
            Keys.TAB)
        time.sleep(2)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_ucMatricula_txtMatricula_CAMPO').send_keys(matricula)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_ucMatricula_txtMatricula_CAMPO').send_keys(Keys.TAB)

        element2 = navegadorBanco.find_element_by_css_selector('#ctl00_UpdPrs')
        while element2.value_of_css_property('display') != 'none':
            time.sleep(1)
            
        time.sleep(6)
    
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_txtRenda_CAMPO').clear()
        time.sleep(2)
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_txtRenda_CAMPO').send_keys(valor_renda())
        time.sleep(0.6)
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_txtRenda_CAMPO').send_keys(Keys.TAB)
        time.sleep(2)

        today = datetime.today()
        first = today.replace(day=1)
        lastMonth = first - timedelta(days=1)
        month = lastMonth.strftime("%m")
        years = lastMonth.strftime("%Y")

        monthLast = month+'/'+years
        monthLast1 = str(monthLast)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_txtDataContraCheque_CAMPO').send_keys(monthLast1)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosIniciais_UcDIni_txtDataContraCheque_CAMPO').send_keys(Keys.TAB)
        time.sleep(2)
        navegadorBanco.find_element_by_id('btnObterMargem_txt').click()
        time.sleep(5)  
        espera_alerta()
        #################################################   CAMPO DADOS PESSOAIS
        time.sleep(1)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtNome_CAMPO').send_keys(nome)
        time.sleep(2)

        if (nacionalidade == 'BRASILEIRA') or (nacionalidade == 'BRASILEIRO'):
            print('true')
        else:
            navegadorBanco.find_element_by_xpath(
                '//*[@id="ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_cbxNacionalidade_CAMPO"]/option[2]').click()
        time.sleep(1.5)
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtNatural_CAMPO').clear()
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtNatural_CAMPO').click()
        time.sleep(1.5)
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtNatural_CAMPO').send_keys(naturalidade)

        time.sleep(1.5)

        if sexo == 'FEMININO':
            navegadorBanco.find_element_by_xpath(
                '//*[@id="ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_cbxSexo_CAMPO"]/option[3]').click()
        else:
            navegadorBanco.find_element_by_xpath(
                '//*[@id="ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_cbxSexo_CAMPO"]/option[2]').click()

        time.sleep(0.5)

        if estadoCivil == 'SOLTEIRO':
            navegadorBanco.find_element_by_css_selector(
            "#ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_cbxEstadoCivil_CAMPO > option:nth-child(2)").click()   
        elif estadoCivil == 'CASADO':
             navegadorBanco.find_element_by_css_selector(
                 '#ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_cbxEstadoCivil_CAMPO > option:nth-child(3)').click()
        elif estadoCivil == 'DESQUITADO':
            navegadorBanco.find_element_by_css_selector(
                '#ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_cbxEstadoCivil_CAMPO > option:nth-child(4)').click()
        elif estadoCivil == 'DIVORCIADO':
            navegadorBanco.find_element_by_css_selector(
                '#ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_cbxEstadoCivil_CAMPO > option:nth-child(5)').click()
        elif estadoCivil == 'VIUVO':
            navegadorBanco.find_element_by_css_selector(
                '#ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_cbxEstadoCivil_CAMPO > option:nth-child(6)').click()
        elif estadoCivil == 'OUTROS':        
            navegadorBanco.find_element_by_css_selector(
                '#ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_cbxEstadoCivil_CAMPO > option:nth-child(7)').click()
        else:
            print('nao escolhido')

        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtDocumento_CAMPO').clear()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtDocumento_CAMPO').send_keys(documento)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtEmissor_CAMPO').clear()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtEmissor_CAMPO').send_keys(orgaoEmissor)
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtDataEmissao_CAMPO').clear()
        time.sleep(0.5)
        navegadorBanco.find_element_by_css_selector(
            "#ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_cbxUFDoc_CAMPO [value='" + doc_uf() + "']").click()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtDataEmissao_CAMPO').send_keys(
            data_doc)
        time.sleep(0.5)
        
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtMae_CAMPO').clear()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtMae_CAMPO').send_keys(mae)
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtDddTelCelular_CAMPO').clear()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtDddTelCelular_CAMPO').send_keys(
            ddd_tel)
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtTelCelular_CAMPO').clear()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnC_txtTelCelular_CAMPO').send_keys(
            numero_tel)
        time.sleep(0.5)
        ############################################## DADOS DO ENDEREÇO
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnCR_txtNumero_CAMPO').clear()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnCR_txtCEP_CAMPO').clear()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnCR_txtCEP_CAMPO').send_keys(cep)
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnCR_txtCEP_CAMPO').send_keys(Keys.TAB)
        time.sleep(2.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnCR_txtEndereco_CAMPO').send_keys(
            logradouro)
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnCR_txtNumero_CAMPO').send_keys(
            numero)
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnCR_txtBairro_CAMPO').send_keys(
            bairro)
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnDadosCliente_UcDadosPessoaisClienteSnt_FIJN1_JnCR_txtCidade_CAMPO').send_keys(
            municipio)
        time.sleep(0.5)
        navegadorBanco.find_element_by_css_selector(
            "#ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_cbxUFBeneficio_CAMPO [value='" + uf_natural() + "']").click()
        time.sleep(0.5)
        ########################################## DADOS DA SIMULAÇAO
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_txtVlrParcela_CAMPO').clear()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_txtVlrParcela_CAMPO').send_keys(
            parcela())
        time.sleep(1)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_UcBtnCalc_btnCalcular_dvCBtn').click()
        time.sleep(5)

        element2 = navegadorBanco.find_element_by_css_selector('#ctl00_UpdPrs')
        while element2.value_of_css_property('display') != 'none':
            time.sleep(1)

        ########################################### CONDIÇOES ESCOLHIDAS

        if len(navegadorBanco.find_elements_by_id('ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_grdCondicoes_ctl02_lblObs')) >= 1:
            final1 = datetime.today()
            final = str(final1)
            fim = (final1 - antes)
            
            navegadorBanco.quit()
            return dumps({ 
                "status":"FORBIDDEN",
                "code":"403",
                "message":"Erro na digitaçao",
                "resultInfo":{
                    "timestamp": str(final),
                    "queryTime":str(fim),
                    "requestId":"e86c6b2ffb60e22c"

            },  
            })
            
        else:
            pass
        
        if opcao == '1':
            navegadorBanco.find_element_by_id(
                'ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_grdCondicoes_ctl02_ckSelecao').click()
        elif opcao == '2':
            navegadorBanco.find_element_by_id(
                'ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_grdCondicoes_ctl03_ckSelecao').click()
        elif opcao == '3':
            navegadorBanco.find_element_by_id(
                'ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_grdCondicoes_ctl04_ckSelecao').click()
        elif opcao == '4':
            navegadorBanco.find_element_by_id(
                'ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_grdCondicoes_ctl05_ckSelecao').click()
        elif opcao == '5':
            navegadorBanco.find_element_by_id(
                'ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_grdCondicoes_ctl06_ckSelecao').click()
        else:
            pyautogui.alert('erro na hora da seleçao de tabela, navegador sera fechado!')
            navegadorBanco.quit()

        time.sleep(3)
        data_venc = navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_UcGridFin_grdFinanciamento_ctl02_Label1').text
        time.sleep(0.5)
        valo_cli = navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_UcGridFin_grdFinanciamento_ctl03_Label1').text
        time.sleep(0.5)
        proposta = ''
        valor_Parcela = navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_UcGridFin_grdFinanciamento_ctl04_Label1').text
        time.sleep(0.5)
        valorFinanciado = navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_UcGridFin_grdFinanciamento_ctl05_Label1').text
        time.sleep(0.5)
        valorBruto = navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_UcGridFin_grdFinanciamento_ctl06_Label1').text
        time.sleep(0.5)
        quantidade_Parcelas = navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_UcGridFin_grdFinanciamento_ctl07_Label1').text
        if quantidade_Parcelas == '084':
            quantidade_Parcelas ='84'
        time.sleep(0.5)
        taxaCLAM1 = navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_UcGridFin_grdFinanciamento_ctl08_Label1').text
        taxaCLAM2 = str(taxaCLAM1).replace(',','.')
        taxaCLAM = taxaCLAM2[:4]
        time.sleep(0.5)
        taxaCETAM1 = navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_UcGridFin_grdFinanciamento_ctl09_Label1').text
        taxaCETAM = str(taxaCETAM1).replace(',','.')
        time.sleep(0.5)
        taxaCETLAA1 = navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnSimulacao_UcSimulacaoSnt_FIJanela1_FIJanelaPanel1_UcGridFin_grdFinanciamento_ctl10_Label1').text
        taxaCETLAA = str(taxaCETLAA1).replace(',','.')
        time.sleep(3.5)

        ######################################## DADOS DA AVERBAÇAO
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_txtBeneficio_CAMPO').clear()
        time.sleep(2)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_txtBeneficio_CAMPO').send_keys(especie)
        time.sleep(2)
        navegadorBanco.find_element_by_css_selector(
            "#ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_cbxUFBeneficio_CAMPO [value='" + text_uf1() + "']").click()
        time.sleep(2)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtBanco_CAMPO').clear()
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtAgencia_CAMPO').clear()
        time.sleep(2)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtBanco_CAMPO').send_keys(banco)
        navegadorBanco.find_element_by_id(
            "ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtBanco_CAMPO").send_keys(
            Keys.TAB)
        ###################################### COLO A AGENCIA DO BANCO ############################
        time.sleep(4)
        navegadorBanco.find_element_by_id(
            "ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtAgencia_CAMPO").send_keys(
            agencia)
        navegadorBanco.find_element_by_id(
            "ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtAgencia_CAMPO").send_keys(
            Keys.TAB)
        time.sleep(2)
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtDvAgencia_CAMPO').send_keys('0')
        time.sleep(4)

        ################################################# CONTA ###############
        ################################################# CONTA ###############
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtConta_CAMPO').click()
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtConta_CAMPO').send_keys(conta)
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            "ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtConta_CAMPO").send_keys(
            Keys.TAB)
        ########################################## DIGITO CONTA
        time.sleep(0.5)
        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtDvConta_CAMPO').send_keys(
            digitoConta)
        navegadorBanco.find_element_by_id(
            "ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_JnC_UcDadosBancarios_txtDvConta_CAMPO").send_keys(
            Keys.TAB)

        time.sleep(3)
        if formaLiberacao == 'TED_CONTA_CORRENTE':
            pass
        elif formaLiberacao == 'TED_CONTA_POUPANCA' :
                print('certo ')
                navegadorBanco.find_element_by_css_selector(
                    "#ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_FIJanelaPanel2_UcDadosPagamento_cbxTipoConta_CAMPO > option:nth-child(2)").click()
        else:
            alert('erro na parte de forma de liberaçao')
            
        ############################################# DIGITA O CPF DO AGENTE #########################

        navegadorBanco.find_element_by_id(
            'ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_FIJanelaPanel3_txtCpfOrigem3o_CAMPO').send_keys(cpfAgente) 
        print('antes')
        time.sleep(4)
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_FIJanelaPanel3_cbxOrigem6_CAMPO_EDIT').click()
        navegadorBanco.find_element_by_id('ctl00_Cph_UcPrp_FIJN1_JnClientes_UcDadosClienteSnt_FIJN1_FIJanelaPanel3_cbxOrigem6_CAMPO_EDIT').send_keys(Keys.TAB)
        time.sleep(3)
        navegadorBanco.find_element_by_id('btnGravar_txt').click()
        final1 = datetime.today()
        time.sleep(5)
        
        try:
            WebDriverWait(navegadorBanco, 30).until(EC.alert_is_present())
            time.sleep(0.5)
            texto = alert.text  
            time.sleep(0.5)              
            proposta1 = texto.split(' ')
            time.sleep(0.5)
            proposta = str(proposta1[6])
            time.sleep(0.5)
            alert.accept()

        except TimeoutException:
            print("no alert")  

        final = str(final1)
        fim = (final1 - antes)   

        navegadorBanco.quit()

        return dumps({ 
            "proposta": str(proposta),
            "dataVencimento": str(data_venc),
            "valorCliente": str(valo_cli),
            "valorParcela": str(valor_Parcela),
            "valorFinanciado": str(valorFinanciado),
            "valorBruto": str(valorBruto),
            "quantidadeParcelas": str(quantidade_Parcelas),
            "taxaCLAM": str(taxaCLAM),
            "taxaCETAM": str(taxaCETAM),
            "taxaCETLAA": str(taxaCETLAA),
            "resultInfo":{
                "timestamp": str(final),
                "queryTime":str(fim),
                "requestId":"e86c6b2ffb60e22c"
        },
            "billingInfo":{
                  "value":"0.4",
                  "charged":'true',
                  "balance":'394.8',
                  "balanceValidUntil":"2021-08-17T00:00:00.000-0300",
                  "subscriptionId":"168gcbc85izyc"
                      } 
        })   
        #########################################  ALERTA FIM  ##############################################   
app.run(host='nome-de-acesso-api')