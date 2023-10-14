public class Main {
    public static void main(String[] args) {
        Game game = new Game();

        game.roll(3);
        game.roll(5);

        int finalScore = game.score();
        System.out.println("Din endelige score: " + finalScore);
    }
    }
