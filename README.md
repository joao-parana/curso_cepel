# curso_cepel 

> repositório referente ao curso de DevSecOps de Claudio Miceli

Para executar os testes usando o **Framework `unittest`** faça:

```bash
python3 -m unittest test.py
```

Erros no repositório remoto (GtHub por exemplo), usado por outros desenvolvedores, 
causam problemas no desenvolvimento colaborativo das equipes.

Se desejar proteger o projeto de forma que o código não vá para para o 
repositório remoto com erros, após `add / commit / push`, use um Hook do Git Localmente.

Veja este exemplo com interceptação do comando `git commit` via Hook local do GIT.

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

Assim ao tentar fazer o commit ele será rejeitado se os testes unitários falharem.

Toda vez que fizer `git push` acesse 
https://github.com/joao-parana/curso_cepel/actions 
para observar aos resultados da execução do Workflow do GitHub Actions
