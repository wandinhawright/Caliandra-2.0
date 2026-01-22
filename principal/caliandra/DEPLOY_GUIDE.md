# Guia de Deploy - Caliandra Django Project

## 📋 Preparação Concluída

✅ Arquivos criados:
- `requirements.txt` - Dependências do projeto
- `.env.example` - Exemplo de variáveis de ambiente
- `Procfile` - Configuração para Render/Heroku
- `runtime.txt` - Versão do Python
- `settings.py` - Atualizado com configurações de produção

## 🚀 Opções de Deploy

### 1. RENDER (RECOMENDADO - Gratuito)

#### Passos:
1. Crie uma conta em https://render.com
2. Instale o Git e inicialize o repositório:
   ```bash
   cd "d:\workspace\caliandra landpage\principal\caliandra"
   git init
   git add .
   git commit -m "Initial commit"
   ```

3. Crie um repositório no GitHub e envie o código:
   ```bash
   git remote add origin https://github.com/seu-usuario/seu-repo.git
   git push -u origin main
   ```

4. No Render:
   - Clique em "New +" → "Web Service"
   - Conecte seu repositório GitHub
   - Configure:
     - **Name**: caliandra
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn caliandra.wsgi:application`
   
5. Adicione variáveis de ambiente:
   - `SECRET_KEY`: gere uma nova chave secreta
   - `DEBUG`: False
   - `ALLOWED_HOSTS`: seu-app.onrender.com
   - `PYTHON_VERSION`: 3.12.0

6. Clique em "Create Web Service"

---

### 2. PYTHONANYWHERE (Gratuito para iniciantes)

#### Passos:
1. Crie uma conta em https://www.pythonanywhere.com
2. No Dashboard, vá em "Web" → "Add a new web app"
3. Escolha "Manual configuration" → Python 3.10
4. Configure o WSGI file:
   - Vá em "Web" → "WSGI configuration file"
   - Edite para apontar para seu projeto Django

5. No console Bash:
   ```bash
   cd ~
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo
   mkvirtualenv --python=/usr/bin/python3.10 meuenv
   pip install -r requirements.txt
   python manage.py collectstatic
   python manage.py migrate
   ```

6. Configure o arquivo WSGI e Static files no painel Web

---

### 3. RAILWAY

1. Acesse https://railway.app
2. Conecte seu repositório GitHub
3. Railway detectará automaticamente o Django
4. Adicione variáveis de ambiente no painel
5. Deploy automático!

---

## 🔧 Antes do Deploy

### 1. Instale as dependências localmente:
```bash
cd "d:\workspace\caliandra landpage\principal\caliandra"
pip install -r requirements.txt
```

### 2. Crie um arquivo `.env` (copie de `.env.example`):
```bash
copy .env.example .env
```

### 3. Gere uma nova SECRET_KEY:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 4. Colete arquivos estáticos:
```bash
python manage.py collectstatic
```

### 5. Execute migrações:
```bash
python manage.py migrate
```

### 6. Teste localmente:
```bash
python manage.py runserver
```

---

## 📝 Checklist de Segurança

- [ ] SECRET_KEY única e segura
- [ ] DEBUG = False em produção
- [ ] ALLOWED_HOSTS configurado
- [ ] Banco de dados de produção (PostgreSQL recomendado)
- [ ] Arquivos estáticos coletados
- [ ] SSL/HTTPS ativado
- [ ] Variáveis sensíveis em .env (não no código)

---

## 🗄️ Database em Produção

Para produção, substitua SQLite por PostgreSQL:

1. No Render/Railway, adicione um banco PostgreSQL
2. Adicione a variável `DATABASE_URL`
3. Instale: `pip install dj-database-url`
4. Em settings.py:
```python
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}
```

---

## 🆘 Problemas Comuns

### Erro 500:
- Verifique logs do servidor
- Confirme DEBUG=False e ALLOWED_HOSTS

### Arquivos estáticos não carregam:
```bash
python manage.py collectstatic --noinput
```

### Banco de dados:
```bash
python manage.py migrate
```

---

## 📞 Recursos Úteis

- Render Docs: https://render.com/docs/deploy-django
- Django Deploy Checklist: https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/
- PythonAnywhere Help: https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/
