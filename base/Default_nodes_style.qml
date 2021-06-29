<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyAlgorithm="0" readOnly="0" hasScaleBasedVisibilityFlag="0" simplifyMaxScale="1" styleCategories="AllStyleCategories" labelsEnabled="1" simplifyDrawingHints="0" simplifyLocal="1" version="3.4.6-Madeira" minScale="1e+08" maxScale="0" simplifyDrawingTol="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" symbollevels="0" type="singleSymbol" enableorderby="0">
    <symbols>
      <symbol clip_to_extent="1" name="0" force_rhr="0" alpha="1" type="marker">
        <layer pass="0" locked="0" enabled="1" class="SimpleMarker">
          <prop k="angle" v="0"/>
          <prop k="color" v="170,0,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="170,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="3"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <labeling type="rule-based">
    <rules key="{90a5cb9d-a69f-48ab-847c-5c2867120643}">
      <rule filter=" &quot;H_NODO_TP2&quot; &lt;> 'NULL' or  &quot;H_NODO_TP2&quot; &lt;> 0" key="{464b58ba-7fcc-4516-ac03-5cf56852f9a4}">
        <settings>
          <text-style fontUnderline="0" previewBkgrdColor="#ffffff" fieldName="'CT= '  || &quot;CT_(N)&quot;  || ' m' ||  '\n'  ||  'h`= '  ||    &#xd;&#xa;round(&quot;H_NODO_TP2&quot;,2) || ' m'" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontSize="8.25" fontLetterSpacing="0" fontFamily="MS Shell Dlg 2" blendMode="0" fontCapitals="0" fontWordSpacing="0" useSubstitutions="0" textColor="170,0,0,255" fontWeight="50" fontItalic="0" multilineHeight="1" fontStrikeout="0" fontSizeUnit="Point" isExpression="1" namedStyle="Normal" textOpacity="1">
            <text-buffer bufferSizeUnits="MapUnit" bufferDraw="1" bufferNoFill="0" bufferJoinStyle="64" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferSize="1" bufferOpacity="0.7" bufferColor="255,255,255,255" bufferBlendMode="0"/>
            <background shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeRadiiUnit="MM" shapeSizeType="0" shapeSizeY="0" shapeDraw="0" shapeBorderWidth="0" shapeJoinStyle="64" shapeType="0" shapeSVGFile="" shapeRotationType="0" shapeSizeUnit="MM" shapeOpacity="1" shapeRadiiX="0" shapeFillColor="255,255,255,255" shapeBorderWidthUnit="MM" shapeOffsetY="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeBorderColor="128,128,128,255" shapeRotation="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiY="0" shapeOffsetUnit="MM" shapeSizeX="0"/>
            <shadow shadowRadiusAlphaOnly="0" shadowOpacity="0.7" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowColor="0,0,0,255" shadowBlendMode="6" shadowOffsetDist="1" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadius="1.5" shadowScale="100" shadowDraw="0" shadowUnder="0" shadowOffsetUnit="MM" shadowOffsetAngle="135" shadowOffsetGlobal="1" shadowRadiusUnit="MM"/>
            <substitutions/>
          </text-style>
          <text-format formatNumbers="0" plussign="0" multilineAlign="0" decimals="3" placeDirectionSymbol="0" autoWrapLength="0" addDirectionSymbol="0" wrapChar="" leftDirectionSymbol="&lt;" reverseDirectionSymbol="0" rightDirectionSymbol=">" useMaxLineLengthForAutoWrap="1"/>
          <placement rotationAngle="0" yOffset="5" distUnits="MapUnit" distMapUnitScale="3x:0,0,0,0,0,0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" offsetType="0" maxCurvedCharAngleOut="-20" placement="0" fitInPolygonOnly="0" xOffset="5" repeatDistanceUnits="MM" priority="5" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" dist="6" preserveRotation="1" maxCurvedCharAngleIn="20" quadOffset="0" placementFlags="10" centroidInside="0" repeatDistance="0" centroidWhole="0" offsetUnits="MM"/>
          <rendering scaleMax="10000000" minFeatureSize="0" scaleVisibility="0" limitNumLabels="0" upsidedownLabels="0" fontLimitPixelSize="0" obstacleFactor="1" drawLabels="1" fontMinPixelSize="3" scaleMin="1" obstacle="1" fontMaxPixelSize="10000" maxNumLabels="2000" zIndex="0" mergeLines="0" displayAll="0" obstacleType="0" labelPerPart="0"/>
          <dd_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="PositionX" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="LABEL_X" name="field" type="QString"/>
                  <Option value="2" name="type" type="int"/>
                </Option>
                <Option name="PositionY" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="LABEL_Y" name="field" type="QString"/>
                  <Option value="2" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </dd_properties>
        </settings>
      </rule>
      <rule filter="ELSE" key="{443567e1-f298-4a78-9de7-c311656e5c23}">
        <settings>
          <text-style fontUnderline="0" previewBkgrdColor="#ffffff" fieldName="'CT='  || &quot;CT_(N)&quot; " fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontSize="8.25" fontLetterSpacing="0" fontFamily="MS Shell Dlg 2" blendMode="0" fontCapitals="0" fontWordSpacing="0" useSubstitutions="0" textColor="170,0,0,255" fontWeight="50" fontItalic="0" multilineHeight="1" fontStrikeout="0" fontSizeUnit="Point" isExpression="1" namedStyle="Normal" textOpacity="1">
            <text-buffer bufferSizeUnits="MapUnit" bufferDraw="1" bufferNoFill="0" bufferJoinStyle="64" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferSize="1" bufferOpacity="0.7" bufferColor="255,255,255,255" bufferBlendMode="0"/>
            <background shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeRadiiUnit="MM" shapeSizeType="0" shapeSizeY="0" shapeDraw="0" shapeBorderWidth="0" shapeJoinStyle="64" shapeType="0" shapeSVGFile="" shapeRotationType="0" shapeSizeUnit="MM" shapeOpacity="1" shapeRadiiX="0" shapeFillColor="255,255,255,255" shapeBorderWidthUnit="MM" shapeOffsetY="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeBorderColor="128,128,128,255" shapeRotation="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiY="0" shapeOffsetUnit="MM" shapeSizeX="0"/>
            <shadow shadowRadiusAlphaOnly="0" shadowOpacity="0.7" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowColor="0,0,0,255" shadowBlendMode="6" shadowOffsetDist="1" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadius="1.5" shadowScale="100" shadowDraw="0" shadowUnder="0" shadowOffsetUnit="MM" shadowOffsetAngle="135" shadowOffsetGlobal="1" shadowRadiusUnit="MM"/>
            <substitutions/>
          </text-style>
          <text-format formatNumbers="0" plussign="0" multilineAlign="0" decimals="3" placeDirectionSymbol="0" autoWrapLength="0" addDirectionSymbol="0" wrapChar="" leftDirectionSymbol="&lt;" reverseDirectionSymbol="0" rightDirectionSymbol=">" useMaxLineLengthForAutoWrap="1"/>
          <placement rotationAngle="0" yOffset="5" distUnits="MapUnit" distMapUnitScale="3x:0,0,0,0,0,0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" offsetType="0" maxCurvedCharAngleOut="-20" placement="0" fitInPolygonOnly="0" xOffset="5" repeatDistanceUnits="MM" priority="5" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" dist="6" preserveRotation="1" maxCurvedCharAngleIn="20" quadOffset="0" placementFlags="10" centroidInside="0" repeatDistance="0" centroidWhole="0" offsetUnits="MM"/>
          <rendering scaleMax="10000000" minFeatureSize="0" scaleVisibility="0" limitNumLabels="0" upsidedownLabels="0" fontLimitPixelSize="0" obstacleFactor="1" drawLabels="1" fontMinPixelSize="3" scaleMin="1" obstacle="1" fontMaxPixelSize="10000" maxNumLabels="2000" zIndex="0" mergeLines="0" displayAll="0" obstacleType="0" labelPerPart="0"/>
          <dd_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="PositionX" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="LABEL_X" name="field" type="QString"/>
                  <Option value="2" name="type" type="int"/>
                </Option>
                <Option name="PositionY" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="LABEL_Y" name="field" type="QString"/>
                  <Option value="2" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </dd_properties>
        </settings>
      </rule>
    </rules>
  </labeling>
  <customproperties>
    <property key="dualview/previewExpressions">
      <value>ID_UC</value>
    </property>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Pie">
    <DiagramCategory opacity="1" barWidth="5" sizeScale="3x:0,0,0,0,0,0" penWidth="0" penColor="#000000" labelPlacementMethod="XHeight" backgroundColor="#ffffff" sizeType="MM" penAlpha="255" width="15" maxScaleDenominator="1e+08" enabled="0" lineSizeScale="3x:0,0,0,0,0,0" lineSizeType="MM" height="15" minimumSize="0" scaleDependency="Area" backgroundAlpha="255" minScaleDenominator="100000" diagramOrientation="Up" rotationOffset="270" scaleBasedVisibility="0">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute label="" color="#000000" field=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings obstacle="0" placement="0" dist="0" showAll="1" linePlacementFlags="2" priority="0" zIndex="0">
    <properties>
      <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties" type="Map">
          <Option name="show" type="Map">
            <Option value="true" name="active" type="bool"/>
            <Option value="AUX05" name="field" type="QString"/>
            <Option value="2" name="type" type="int"/>
          </Option>
        </Option>
        <Option value="collection" name="type" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="CT_(N)">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ID_UC">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="AUX04">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="AUX05">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="AUX06">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="LABEL_X">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="LABEL_Y">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="LABEL_VIS">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="CF_NODO_2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="H_NODO_TP2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias index="0" name="" field="CT_(N)"/>
    <alias index="1" name="" field="ID_UC"/>
    <alias index="2" name="" field="AUX04"/>
    <alias index="3" name="" field="AUX05"/>
    <alias index="4" name="" field="AUX06"/>
    <alias index="5" name="" field="LABEL_X"/>
    <alias index="6" name="" field="LABEL_Y"/>
    <alias index="7" name="" field="LABEL_VIS"/>
    <alias index="8" name="" field="CF_NODO_2"/>
    <alias index="9" name="" field="H_NODO_TP2"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" applyOnUpdate="0" field="CT_(N)"/>
    <default expression="" applyOnUpdate="0" field="ID_UC"/>
    <default expression="" applyOnUpdate="0" field="AUX04"/>
    <default expression="" applyOnUpdate="0" field="AUX05"/>
    <default expression="" applyOnUpdate="0" field="AUX06"/>
    <default expression="" applyOnUpdate="0" field="LABEL_X"/>
    <default expression="" applyOnUpdate="0" field="LABEL_Y"/>
    <default expression="" applyOnUpdate="0" field="LABEL_VIS"/>
    <default expression="" applyOnUpdate="0" field="CF_NODO_2"/>
    <default expression="" applyOnUpdate="0" field="H_NODO_TP2"/>
  </defaults>
  <constraints>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="CT_(N)"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="ID_UC"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="AUX04"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="AUX05"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="AUX06"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="LABEL_X"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="LABEL_Y"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="LABEL_VIS"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="CF_NODO_2"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="H_NODO_TP2"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="CT_(N)"/>
    <constraint exp="" desc="" field="ID_UC"/>
    <constraint exp="" desc="" field="AUX04"/>
    <constraint exp="" desc="" field="AUX05"/>
    <constraint exp="" desc="" field="AUX06"/>
    <constraint exp="" desc="" field="LABEL_X"/>
    <constraint exp="" desc="" field="LABEL_Y"/>
    <constraint exp="" desc="" field="LABEL_VIS"/>
    <constraint exp="" desc="" field="CF_NODO_2"/>
    <constraint exp="" desc="" field="H_NODO_TP2"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortOrder="1" actionWidgetStyle="dropDown" sortExpression="&quot;H_NODO_TP2&quot;">
    <columns>
      <column width="-1" name="AUX05" hidden="0" type="field"/>
      <column width="-1" name="AUX04" hidden="0" type="field"/>
      <column width="-1" name="AUX06" hidden="0" type="field"/>
      <column width="-1" name="LABEL_VIS" hidden="0" type="field"/>
      <column width="-1" name="CT_(N)" hidden="0" type="field"/>
      <column width="-1" name="LABEL_X" hidden="0" type="field"/>
      <column width="-1" name="LABEL_Y" hidden="0" type="field"/>
      <column width="-1" name="ID_UC" hidden="0" type="field"/>
      <column width="-1" hidden="1" type="actions"/>
      <column width="-1" name="CF_NODO_2" hidden="0" type="field"/>
      <column width="-1" name="H_NODO_TP2" hidden="0" type="field"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1">D:/_ARQUIVOS_P/RedBasica_2/_Produto02 - Melhorias01/Cap Haitien - Inicio Zero - Copia</editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath>D:/_ARQUIVOS_P/RedBasica_2/_Produto02 - Melhorias01/Cap Haitien - Inicio Zero - Copia</editforminitfilepath>
  <editforminitcode><![CDATA[# -*- codificação: utf-8 -*-
"""
Os formulários do QGIS podem ter uma função Python que é chamada quando
o formulário
 é aberto.

QGIS forms can have a Python function that is called when the form is
opened.

Use esta função para adicionar lógica extra aos seus formulários.

Entre com o nome da função no campo "Python Init function".
Un exemplo a seguir:
"""
a partir de PyQt4.QtGui importe QWidget

def my_form_open(diálogo, camada, feição):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>1</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="AUX04" editable="1"/>
    <field name="AUX05" editable="1"/>
    <field name="AUX06" editable="1"/>
    <field name="CF_NODO_2" editable="1"/>
    <field name="CF_nodo" editable="1"/>
    <field name="CItrd_nodo" editable="1"/>
    <field name="CT_(N)" editable="1"/>
    <field name="H_NODO_TP2" editable="1"/>
    <field name="ID_UC" editable="1"/>
    <field name="Id_NODO_(n" editable="1"/>
    <field name="LABEL_VIS" editable="1"/>
    <field name="LABEL_X" editable="1"/>
    <field name="LABEL_Y" editable="1"/>
    <field name="Nodo_tipo" editable="1"/>
    <field name="Tap_nodo" editable="1"/>
    <field name="h_nodo_NT" editable="1"/>
    <field name="h_nodo_tp" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="AUX04" labelOnTop="0"/>
    <field name="AUX05" labelOnTop="0"/>
    <field name="AUX06" labelOnTop="0"/>
    <field name="CF_NODO_2" labelOnTop="0"/>
    <field name="CF_nodo" labelOnTop="0"/>
    <field name="CItrd_nodo" labelOnTop="0"/>
    <field name="CT_(N)" labelOnTop="0"/>
    <field name="H_NODO_TP2" labelOnTop="0"/>
    <field name="ID_UC" labelOnTop="0"/>
    <field name="Id_NODO_(n" labelOnTop="0"/>
    <field name="LABEL_VIS" labelOnTop="0"/>
    <field name="LABEL_X" labelOnTop="0"/>
    <field name="LABEL_Y" labelOnTop="0"/>
    <field name="Nodo_tipo" labelOnTop="0"/>
    <field name="Tap_nodo" labelOnTop="0"/>
    <field name="h_nodo_NT" labelOnTop="0"/>
    <field name="h_nodo_tp" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>ID_UC</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
