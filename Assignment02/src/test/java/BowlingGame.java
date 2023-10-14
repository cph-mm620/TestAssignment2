import cucumber.api.java.en.Given;
import cucumber.api.java.en.When;
import cucumber.api.java.en.Then;
import org.junit.Assert;

public class BowlingGame {
    Game g;
    int result = 0;
    @Given("there is a game to join")
    public void thereIsAGameToJoin() {
        g = new Game();
    }
    @When("zero pins are hit")
    public void zeroPinsAreHit() {
        rollMany(20, 0);
        result = g.score();
    }
    @When("one pin is hit every roll")
    public void onePinIsHitEveryRoll() {
        rollMany(20, 1);
        result = g.score();
    }
    @When("one spare is made and the bonus roll is {int}")
    public void oneSpareIsMadeAndTheBonusRollIs(int arg0) {
        rollSpare();
        g.roll(3);
        rollMany(17, 0);
        result = g.score();
    }
    @When("one strike is made and the bonus rolls are {int} and {int}")
    public void oneStrikeIsMadeAndTheBonusRollsAreAnd(int bonusRoll1, int bonusRoll2) {
        rollStrike();
        g.roll(bonusRoll1);
        g.roll(bonusRoll2);
        rollMany(16, 0);
        result = g.score();
    }
    @When("only strikes are made")
    public void onlyStrikesAreMade() {
        rollMany(12, 10);
        result = g.score();
    }
    @Then("the result should be {int};")
    public void theResultShouldBe(int expected) {
        Assert.assertEquals(expected, result);
    }
    private void rollMany(int n, int pins) {
        for (int i = 0; i < n; i++) {
            g.roll(pins);
        }
    }
    private void rollStrike() {
        g.roll(10);
    }

    private void rollSpare() {
        g.roll(5);
        g.roll(5);
    }
}