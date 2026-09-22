# Exercícios de Python

Quatro exercícios acadêmicos de fundamentos de programação, desenvolvidos durante a graduação em Análise e Desenvolvimento de Sistemas no CEUB.

O foco é praticar **laços `while`, contadores e acumuladores**. São programas de terminal, sem bibliotecas externas.

## Executar

Instale Python 3 e Git. No terminal:

```bash
git clone https://github.com/gabrieldalmeida0/python-exercises.git
cd python-exercises
python sequence_ascending.py
```

Em sistemas que usam `python3`, substitua `python` por `python3`. No Windows, `py` também pode estar disponível. Confira a instalação com `python --version`.

## Arquivos e exemplos

| Arquivo | Entrada | Resultado esperado |
| --- | --- | --- |
| [sequence_ascending.py](sequence_ascending.py) | `3` | Sequência `1 2 3`; quantidade `3`. |
| [sequence_descending.py](sequence_descending.py) | `3` | Sequência `3 2 1 0`; quantidade `4`. |
| [sum_1_to_500.py](sum_1_to_500.py) | Não solicita entrada | Soma `125250`; quantidade `500`. |
| [sum_arithmetic_progression.py](sum_arithmetic_progression.py) | Não solicita entrada | Soma `20667`; quantidade `83`. |

Para executar outro exercício, troque o nome do arquivo no comando.

### Exemplo interativo

```text
Digite o número final (inteiro a partir de 1): 3
Sequência:
1 2 3
Quantidade: 3
```

## Regras de entrada

- A sequência crescente aceita inteiros a partir de `1`.
- A sequência decrescente aceita inteiros a partir de `0`; com zero, exibe `0` e quantidade `1`.
- Texto, números fracionários e valores abaixo do mínimo geram uma orientação e uma nova tentativa.
- A progressão aritmética começa em `3`, avança de `6` em `6` e termina em `495`, último termo menor ou igual a `500`.
- Use valores pequenos nos exercícios interativos: cada elemento é impresso no terminal. Para interromper, pressione `Ctrl+C`.

## Escopo

Este repositório apresenta exercícios introdutórios. A validação de entrada foi acrescentada para tornar a execução mais clara, preservando a resolução com `while`.
