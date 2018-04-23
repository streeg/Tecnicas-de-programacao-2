import br.unb.cic.epl.Core
import br.unb.cic.epl.Eval
import br.unb.cic.epl.Add
import br.unb.cic.epl.AddEval
import br.unb.cic.epl.Sub
import br.unb.cic.epl.SubEval
import br.unb.cic.epl.Mult
import br.unb.cic.epl.MultEval

object Main extends App {
  val lit100 = new Core.Literal(100) with Eval.Literal
  val lit500 = new Core.Literal(500) with Eval.Literal

  val sum = new Add.Add(lit100, lit500) 
  val sub = new Sub.Sub(lit500, lit100)
  val mult = new Mult.Mult(lit500, lit100)

  println(sum.print())
  println(sub.print())
  println(mult.print())
  println(lit100.eval())

}
