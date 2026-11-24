/*
Disciplina : 2026-PCAP
Projeto    : MeuApp v5.0 - o Fliperama em Java (Aula 33)
Autor      : Luanny Cubas
LIAC       : Menu com validacao, cadastro de jogadores em fichas numa lista que cresce, e um jogo que conta as partidas de que jogou.
Data       : 2026.11.24
*/
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

class Jogador {
    String apelido;
    int partidas;
}

public class fliperama {
    static final String DONO = "LUANNY.PANDA";
    static Scanner teclado = new Scanner(System.in);
    static Random sorteio = new Random();

    static void linha() {
        System.out.println("-------------------------------");
    }

    static void titulo(String texto) {
        linha();
        System.out.println("    " + texto);
        linha();
    }
    static int lerInteiro() {
        int numero = -1;

        if (teclado.hasNextInt()) {
            numero = teclado.nextInt();
        }
        teclado.nextLine();
        return numero;
    }

    static int lerNumero(String mensagem, int minimo, int maximo) {
        int numero;

        System.out.print(mensagem + ": ");
        numero = lerInteiro();
        while (numero < minimo || numero > maximo) {
            System.out.print("Opcao invalida! Tente de novo: ");
            numero = lerInteiro();
        }
        return numero;
    }

    static String lerTexto(String mensagem) {
        System.out.print(mensagem + ": ");
        return teclado.nextLine();
    }

    static int buscar(ArrayList<Jogador> jogadores, String procurado) {
        int i, qtd = jogadores.size();

        for(i = 0; i < qtd; i++) {
            if (jogadores.get(i).apelido.equals(procurado)) {
                return i;
            }
        }
        return -1;
    }

    static void cadastrar(ArrayList<Jogador> jogadores) {
        Jogador novo = new Jogador();

        titulo("NOVO JOGADOR");
        novo.apelido = lerTexto("Apelido");
        novo.partidas = 0;
        jogadores.add(novo);
        System.out.println("Jogador " + novo.apelido + " cadastrado.");
    }

    static void listar(ArrayList<Jogador> jogadores) {
        Jogador j;
        int i, qtd = jogadores.size();

        titulo("JOGADORES CADASTRADOS");
        if (qtd == 0) {
            System.out.println("Nenhum jogador cadastrado ainda.");
        }
        for (i = 0; i < qtd; i++) {
            j = jogadores.get(i);
            System.out.println(j.apelido + " | " + j.partidas + " partidas");
        }
    }

    static void JogarAdivinhe(ArrayList<Jogador> jogadores) {
        Jogador jogador;
        String quem;
        int pos, segredo, palpite, tentativas;

        titulo("ADIVINHE O NUMERO");
        quem = lerTexto("Quem vai jogar");
        pos = buscar(jogadores, quem);
        if (pos == -1) {
            System.out.println("Cadastre esse apelido antes de jogar.");
            return;
        }

        segredo = sorteio.nextInt(100) + 1;
        System.out.println("Pensei num numero de 1 a 100.");

        palpite = lerNumero("Seu palpite", 1, 100);
        tentativas = 1;
        while (palpite != segredo) {
            if (palpite < segredo) {
                System.out.println("Maior!");
            } else {
                System.out.println("Menor!");
            }
            palpite = lerNumero("Seu palpite", 1, 100);
            tentativas = tentativas + 1;
        }
        System.out.println("Acertou em " + tentativas + " tentativas, " + quem + "!");

        jogador = jogadores.get(pos);
        jogador.partidas = jogador.partidas + 1;
    }

    static void mostrarMenu() {
        linha();
        System.out.println("    FLIPERAMA DA " + DONO);
        linha();
        System.out.println("[1] Adivinhe o Numero");
        System.out.println("[2] Cadastrar jogador");
        System.out.println("[3] Litar jogadores");
        System.out.println("[0] Sair");
        linha();
    }

    public static void main(String[] args) {
        ArrayList<Jogador> jogadores = new ArrayList<Jogador>();
        int opcao;

        mostrarMenu();
        opcao = lerNumero("Sua escolha", 0, 3);
        while (opcao != 0) {
            if (opcao == 1) {
                JogarAdivinhe(jogadores);
            } else if (opcao == 2) {
                cadastrar(jogadores);
            } else {
                listar(jogadores);
            }
            mostrarMenu();
            opcao = lerNumero("Sua escolha", 0, 3);
        }

        titulo("Ate a proxima!");
    }
}