/**
 * indicadores
 * indicadores trm, uf, utm
 *
 * OpenAPI spec version: 1.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */
package io.swagger.client.api

import io.swagger.client.model.Empty
import io.swagger.client.core._
import io.swagger.client.core.CollectionFormats._
import io.swagger.client.core.ApiKeyLocations._

object DefaultApi {

  /**
   * 
   * 
   * Expected answers:
   *   code 200 : Empty (200 response)
   */
  def indicadoreshoyGet(): ApiRequest[Empty] =
    ApiRequest[Empty](ApiMethods.GET, "https://vgi1o4pkrc.execute-api.us-east-2.amazonaws.com/Prod", "/indicadoreshoy", "application/json")
      .withSuccessResponse[Empty](200)
        /**
   * 
   * 
   * Expected answers:
   *   code 200 : Empty (200 response)
   *              Headers :
   *                Access-Control-Allow-Origin - 
   *                Access-Control-Allow-Methods - 
   *                Access-Control-Allow-Headers - 
   */
  def indicadoreshoyOptions(): ApiRequest[Empty] =
    ApiRequest[Empty](ApiMethods.OPTIONS, "https://vgi1o4pkrc.execute-api.us-east-2.amazonaws.com/Prod", "/indicadoreshoy", "application/json")
      .withSuccessResponse[Empty](200)
      
  object IndicadoreshoyOptionsHeaders { 
    def accessControlAllowOrigin(r: ApiReturnWithHeaders) = r.getStringHeader("Access-Control-Allow-Origin")
    def accessControlAllowMethods(r: ApiReturnWithHeaders) = r.getStringHeader("Access-Control-Allow-Methods")
    def accessControlAllowHeaders(r: ApiReturnWithHeaders) = r.getStringHeader("Access-Control-Allow-Headers")
  }


}

