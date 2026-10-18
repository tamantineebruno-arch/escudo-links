# escudo-links

Links permanentes de redirecionamento das plaquinhas NFC do **Escudo de Reputação**
(Almeida Soluções Digitais).

## Como funciona

O QR impresso na plaquinha e a tag NFC apontam para um endereço deste repositório
(ex.: `https://tamantineebruno-arch.github.io/escudo-links/hortifruti/`), que
redireciona para o destino real (avaliação no Google, Instagram, WhatsApp...).

Se o destino mudar, basta editar o HTML da pasta do cliente — **a plaquinha
continua funcionando, sem reimpressão**.

## Adicionar um cliente

```bash
python3 adicionar_cliente.py --slug hortifruti --url "https://link-de-avaliacao-do-google"
```

## Testar

Abra `https://tamantineebruno-arch.github.io/escudo-links/demo/` no celular.
