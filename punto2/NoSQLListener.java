// Generated from NoSQL.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link NoSQLParser}.
 */
public interface NoSQLListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link NoSQLParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(NoSQLParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link NoSQLParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(NoSQLParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link NoSQLParser#sentencia}.
	 * @param ctx the parse tree
	 */
	void enterSentencia(NoSQLParser.SentenciaContext ctx);
	/**
	 * Exit a parse tree produced by {@link NoSQLParser#sentencia}.
	 * @param ctx the parse tree
	 */
	void exitSentencia(NoSQLParser.SentenciaContext ctx);
	/**
	 * Enter a parse tree produced by {@link NoSQLParser#insertar}.
	 * @param ctx the parse tree
	 */
	void enterInsertar(NoSQLParser.InsertarContext ctx);
	/**
	 * Exit a parse tree produced by {@link NoSQLParser#insertar}.
	 * @param ctx the parse tree
	 */
	void exitInsertar(NoSQLParser.InsertarContext ctx);
	/**
	 * Enter a parse tree produced by {@link NoSQLParser#buscar}.
	 * @param ctx the parse tree
	 */
	void enterBuscar(NoSQLParser.BuscarContext ctx);
	/**
	 * Exit a parse tree produced by {@link NoSQLParser#buscar}.
	 * @param ctx the parse tree
	 */
	void exitBuscar(NoSQLParser.BuscarContext ctx);
	/**
	 * Enter a parse tree produced by {@link NoSQLParser#actualizar}.
	 * @param ctx the parse tree
	 */
	void enterActualizar(NoSQLParser.ActualizarContext ctx);
	/**
	 * Exit a parse tree produced by {@link NoSQLParser#actualizar}.
	 * @param ctx the parse tree
	 */
	void exitActualizar(NoSQLParser.ActualizarContext ctx);
	/**
	 * Enter a parse tree produced by {@link NoSQLParser#eliminar}.
	 * @param ctx the parse tree
	 */
	void enterEliminar(NoSQLParser.EliminarContext ctx);
	/**
	 * Exit a parse tree produced by {@link NoSQLParser#eliminar}.
	 * @param ctx the parse tree
	 */
	void exitEliminar(NoSQLParser.EliminarContext ctx);
	/**
	 * Enter a parse tree produced by {@link NoSQLParser#filtro}.
	 * @param ctx the parse tree
	 */
	void enterFiltro(NoSQLParser.FiltroContext ctx);
	/**
	 * Exit a parse tree produced by {@link NoSQLParser#filtro}.
	 * @param ctx the parse tree
	 */
	void exitFiltro(NoSQLParser.FiltroContext ctx);
	/**
	 * Enter a parse tree produced by {@link NoSQLParser#proyeccion}.
	 * @param ctx the parse tree
	 */
	void enterProyeccion(NoSQLParser.ProyeccionContext ctx);
	/**
	 * Exit a parse tree produced by {@link NoSQLParser#proyeccion}.
	 * @param ctx the parse tree
	 */
	void exitProyeccion(NoSQLParser.ProyeccionContext ctx);
	/**
	 * Enter a parse tree produced by {@link NoSQLParser#limite}.
	 * @param ctx the parse tree
	 */
	void enterLimite(NoSQLParser.LimiteContext ctx);
	/**
	 * Exit a parse tree produced by {@link NoSQLParser#limite}.
	 * @param ctx the parse tree
	 */
	void exitLimite(NoSQLParser.LimiteContext ctx);
	/**
	 * Enter a parse tree produced by {@link NoSQLParser#actualizacion}.
	 * @param ctx the parse tree
	 */
	void enterActualizacion(NoSQLParser.ActualizacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link NoSQLParser#actualizacion}.
	 * @param ctx the parse tree
	 */
	void exitActualizacion(NoSQLParser.ActualizacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link NoSQLParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void enterAsignacion(NoSQLParser.AsignacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link NoSQLParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void exitAsignacion(NoSQLParser.AsignacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link NoSQLParser#documento}.
	 * @param ctx the parse tree
	 */
	void enterDocumento(NoSQLParser.DocumentoContext ctx);
	/**
	 * Exit a parse tree produced by {@link NoSQLParser#documento}.
	 * @param ctx the parse tree
	 */
	void exitDocumento(NoSQLParser.DocumentoContext ctx);
	/**
	 * Enter a parse tree produced by {@link NoSQLParser#par}.
	 * @param ctx the parse tree
	 */
	void enterPar(NoSQLParser.ParContext ctx);
	/**
	 * Exit a parse tree produced by {@link NoSQLParser#par}.
	 * @param ctx the parse tree
	 */
	void exitPar(NoSQLParser.ParContext ctx);
	/**
	 * Enter a parse tree produced by {@link NoSQLParser#valor}.
	 * @param ctx the parse tree
	 */
	void enterValor(NoSQLParser.ValorContext ctx);
	/**
	 * Exit a parse tree produced by {@link NoSQLParser#valor}.
	 * @param ctx the parse tree
	 */
	void exitValor(NoSQLParser.ValorContext ctx);
	/**
	 * Enter a parse tree produced by {@link NoSQLParser#condicion}.
	 * @param ctx the parse tree
	 */
	void enterCondicion(NoSQLParser.CondicionContext ctx);
	/**
	 * Exit a parse tree produced by {@link NoSQLParser#condicion}.
	 * @param ctx the parse tree
	 */
	void exitCondicion(NoSQLParser.CondicionContext ctx);
	/**
	 * Enter a parse tree produced by {@link NoSQLParser#campo}.
	 * @param ctx the parse tree
	 */
	void enterCampo(NoSQLParser.CampoContext ctx);
	/**
	 * Exit a parse tree produced by {@link NoSQLParser#campo}.
	 * @param ctx the parse tree
	 */
	void exitCampo(NoSQLParser.CampoContext ctx);
	/**
	 * Enter a parse tree produced by {@link NoSQLParser#op}.
	 * @param ctx the parse tree
	 */
	void enterOp(NoSQLParser.OpContext ctx);
	/**
	 * Exit a parse tree produced by {@link NoSQLParser#op}.
	 * @param ctx the parse tree
	 */
	void exitOp(NoSQLParser.OpContext ctx);
}