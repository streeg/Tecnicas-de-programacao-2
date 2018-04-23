package br.unb.cic.epl

import org.scalatest.FlatSpec
import org.scalatest.Matchers
import org.scalatest.GivenWhenThen
import org.scalatest.BeforeAndAfter


class TestSub extends FlatSpec with Matchers with GivenWhenThen with BeforeAndAfter {

  behavior of "An Sub expression"

  var literal100: Eval.Literal = _
  var literal200: Eval.Literal = _

  before {
    literal100 = new Core.Literal(200) with Eval.Literal
    literal200 = new Core.Literal(50) with Eval.Literal
  }

  it should "return String (200 - 50) when we call Sub(Literal(200), Literal(50).print())" in {
    val sub = new SubEval.Sub(literal200, literal50)
  
    sub.print() should be ("(200 - 50)")
  }

  it should "return 150 when we call call Sub(Literal(200), Literal(50)).eval()" in {
    val sub = new SubEval.Sub(literal200, literal50)

    sub.eval() should be (150)
  }
}
