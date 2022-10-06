# curso_cepel 


> repositório referente ao curso de DevSecOps de Claudio Miceli

## Testes unitários

Para executar os testes usando o **Framework `unittest`** faça:

```bash
python3 -m unittest test.py
```

## Interceptando eventos no git

**Motivação:**

Erros no repositório remoto (GtHub por exemplo), usado por outros desenvolvedores, 
causam problemas no desenvolvimento colaborativo das equipes.

**Problema:**

Você deseja proteger o projeto de forma que o código alterado não vá para para o 
repositório remoto com erros após a execução dos comandos `add / commit / push`

**Solução**

Use um Hook do Git Localmente. Veja este exemplo com interceptação do comando `git commit` via Hook local do GIT.

```bash
cat .git/hooks/pre-commit
```

```bash
#!/bin/sh

echo "GIT: Running pre-commit"
echo "----------------------------------------------------------"

python3 -m unittest test*.py

if [ $? -eq 0 ]
then
  echo "Test pass successfully"
else
  echo "Test doesn't pass. Commit aborted"
  exit 100
fi
```

Observe que a shell Bash de pré-commit retorna valor **diferente de zero** quando o teste falha. Isto é suficiente para o commit ser abortado.

Assim ao tentar fazer o commit ele será rejeitado se os testes unitários falharem.

## Verificando as actions.

Toda vez que fizer `git push` acesse 
https://github.com/joao-parana/curso_cepel/actions 
para observar aos resultados da execução do Workflow do GitHub Actions
