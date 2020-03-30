<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyDrawingHints="0" minScale="1e+08" simplifyMaxScale="1" labelsEnabled="1" simplifyLocal="1" simplifyDrawingTol="1" styleCategories="AllStyleCategories" maxScale="100000" hasScaleBasedVisibilityFlag="0" version="3.4.4-Madeira" simplifyAlgorithm="0" readOnly="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" enableorderby="0" symbollevels="0" type="singleSymbol">
    <symbols>
      <symbol name="0" force_rhr="0" clip_to_extent="1" alpha="1" type="marker">
        <layer enabled="1" class="GeometryGenerator" locked="0" pass="0">
          <prop k="SymbolType" v="Line"/>
          <prop k="geometryModifier" v="CASE &#xd;&#xa;WHEN @map_scale &lt; 2500 and (&quot;LABEL_VIS&quot; &lt;> 0)&#xd;&#xa;THEN&#xd;&#xa;&#xd;&#xa;If ($x &lt; &quot;LABEL_X&quot;,&#xd;&#xa;&#xd;&#xa;make_line (&#xd;&#xa;make_point( &quot;LABEL_X&quot; + (0.0155 * @map_scale), &quot;LABEL_Y&quot; + (0.0037 * @map_scale)),&#xd;&#xa;make_point( &quot;LABEL_X&quot; - (0.0020 * @map_scale), &quot;LABEL_Y&quot; + (0.0037 * @map_scale)),&#xd;&#xa;make_point( x(centroid( $geometry )), y(centroid( $geometry )))&#xd;&#xa; ),&#xd;&#xa; &#xd;&#xa;make_line (&#xd;&#xa;make_point( &quot;LABEL_X&quot; - (0.0010 * @map_scale), &quot;LABEL_Y&quot; + (0.0037 * @map_scale)),&#xd;&#xa;make_point( &quot;LABEL_X&quot; + (0.0155 * @map_scale), &quot;LABEL_Y&quot; + (0.0037 * @map_scale)),&#xd;&#xa;make_point( x(centroid( $geometry )), y(centroid( $geometry )))&#xd;&#xa; )&#xd;&#xa; &#xd;&#xa; )&#xd;&#xa; &#xd;&#xa; END"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol name="@0@0" force_rhr="0" clip_to_extent="1" alpha="1" type="line">
            <layer enabled="1" class="SimpleLine" locked="0" pass="0">
              <prop k="capstyle" v="square"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="customdash_unit" v="MM"/>
              <prop k="draw_inside_polygon" v="0"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="line_color" v="0,0,0,255"/>
              <prop k="line_style" v="solid"/>
              <prop k="line_width" v="0.3"/>
              <prop k="line_width_unit" v="MM"/>
              <prop k="offset" v="0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="ring_filter" v="0"/>
              <prop k="use_custom_dash" v="0"/>
              <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties"/>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer enabled="1" class="SimpleMarker" locked="0" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="170,0,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <labeling type="rule-based">
    <rules key="{77ae875e-46ba-49c2-94c4-b9eb696963fb}">
      <rule key="{75574758-3fd0-49d0-aaad-ea80082fd46f}">
        <settings>
          <text-style previewBkgrdColor="#ffffff" fontWeight="50" namedStyle="Normal" fontSizeUnit="Point" blendMode="0" fontItalic="0" fieldName=" &#x9;  'CT  '  ||&quot;CT_(N)&quot;  ||  '\n'   ||  &#xd;&#xa;&#x9;   'CF  '  ||&quot;CF_nodo&quot;&#xd;&#xa;" fontUnderline="0" fontStrikeout="0" fontFamily="MS Shell Dlg 2" textColor="0,0,0,255" fontWordSpacing="0" fontLetterSpacing="0" isExpression="1" fontSize="8.25" multilineHeight="1.2" fontCapitals="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" useSubstitutions="0" textOpacity="1">
            <text-buffer bufferNoFill="0" bufferSizeUnits="MM" bufferColor="255,255,255,255" bufferBlendMode="0" bufferSize="0.8" bufferOpacity="1" bufferDraw="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferJoinStyle="128"/>
            <background shapeSizeType="0" shapeBorderColor="128,128,128,255" shapeBorderWidthUnit="MM" shapeRotation="0" shapeOffsetY="0" shapeSizeX="0" shapeSizeY="0" shapeRadiiUnit="MM" shapeSizeUnit="MM" shapeRadiiX="0" shapeFillColor="255,255,255,255" shapeBorderWidth="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeJoinStyle="64" shapeRotationType="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeDraw="0" shapeOffsetUnit="MM" shapeSVGFile="" shapeRadiiY="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeType="0" shapeOpacity="1" shapeOffsetX="0"/>
            <shadow shadowOpacity="0.7" shadowOffsetAngle="135" shadowOffsetDist="1" shadowRadius="1.5" shadowRadiusAlphaOnly="0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetUnit="MM" shadowUnder="0" shadowScale="100" shadowDraw="0" shadowOffsetGlobal="1" shadowColor="0,0,0,255" shadowBlendMode="6" shadowRadiusUnit="MM"/>
            <substitutions/>
          </text-style>
          <text-format placeDirectionSymbol="0" formatNumbers="0" useMaxLineLengthForAutoWrap="1" autoWrapLength="0" decimals="3" rightDirectionSymbol=">" plussign="0" addDirectionSymbol="0" wrapChar="" reverseDirectionSymbol="0" multilineAlign="0" leftDirectionSymbol="&lt;"/>
          <placement preserveRotation="1" repeatDistanceUnits="MM" placement="0" placementFlags="10" fitInPolygonOnly="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" rotationAngle="0" distMapUnitScale="3x:0,0,0,0,0,0" offsetType="0" yOffset="0" maxCurvedCharAngleOut="-25" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleIn="25" centroidWhole="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" priority="5" dist="0" centroidInside="0" distUnits="MM" repeatDistance="0" quadOffset="4" offsetUnits="MapUnit" xOffset="0"/>
          <rendering obstacle="1" scaleMin="1" limitNumLabels="0" upsidedownLabels="0" fontLimitPixelSize="0" mergeLines="0" fontMaxPixelSize="10000" obstacleFactor="1" labelPerPart="0" drawLabels="1" minFeatureSize="0" maxNumLabels="50" fontMinPixelSize="3" zIndex="0" obstacleType="0" displayAll="0" scaleVisibility="1" scaleMax="2500"/>
          <dd_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="PositionX" type="Map">
                  <Option name="active" value="true" type="bool"/>
                  <Option name="field" value="LABEL_X" type="QString"/>
                  <Option name="type" value="2" type="int"/>
                </Option>
                <Option name="PositionY" type="Map">
                  <Option name="active" value="true" type="bool"/>
                  <Option name="field" value="LABEL_Y" type="QString"/>
                  <Option name="type" value="2" type="int"/>
                </Option>
                <Option name="Show" type="Map">
                  <Option name="active" value="true" type="bool"/>
                  <Option name="field" value="LABEL_VIS" type="QString"/>
                  <Option name="type" value="2" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </dd_properties>
        </settings>
      </rule>
      <rule key="{733a4e23-a43c-44cf-be50-c8e027cbb7d4}">
        <settings>
          <text-style previewBkgrdColor="#ffffff" fontWeight="50" namedStyle="Normal" fontSizeUnit="Point" blendMode="0" fontItalic="0" fieldName="If (&#xd;&#xa;&#xd;&#xa;&#x9;$x &lt; &quot;LABEL_X&quot;, &#xd;&#xa;&#x9;&#xd;&#xa;&#x9;&quot;h_nodo_NT&quot;  ||'  '||  &quot;Nodo_tipo&quot;,&#xd;&#xa;&#xd;&#xa;&#x9; &quot;Nodo_tipo&quot; ||'  '||&quot;h_nodo_NT&quot; &#xd;&#xa;&#x9;&#xd;&#xa;&#x9;)" fontUnderline="0" fontStrikeout="0" fontFamily="MS Shell Dlg 2" textColor="0,0,0,255" fontWordSpacing="-3" fontLetterSpacing="0" isExpression="1" fontSize="8.25" multilineHeight="1" fontCapitals="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" useSubstitutions="0" textOpacity="1">
            <text-buffer bufferNoFill="0" bufferSizeUnits="MM" bufferColor="255,255,255,255" bufferBlendMode="0" bufferSize="0.8" bufferOpacity="1" bufferDraw="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferJoinStyle="128"/>
            <background shapeSizeType="0" shapeBorderColor="128,128,128,255" shapeBorderWidthUnit="MM" shapeRotation="0" shapeOffsetY="0" shapeSizeX="0" shapeSizeY="0" shapeRadiiUnit="MM" shapeSizeUnit="MM" shapeRadiiX="0" shapeFillColor="255,255,255,255" shapeBorderWidth="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeJoinStyle="64" shapeRotationType="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeDraw="0" shapeOffsetUnit="MM" shapeSVGFile="" shapeRadiiY="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeType="0" shapeOpacity="1" shapeOffsetX="0"/>
            <shadow shadowOpacity="0.7" shadowOffsetAngle="135" shadowOffsetDist="1" shadowRadius="1.5" shadowRadiusAlphaOnly="0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetUnit="MM" shadowUnder="0" shadowScale="100" shadowDraw="0" shadowOffsetGlobal="1" shadowColor="0,0,0,255" shadowBlendMode="6" shadowRadiusUnit="MM"/>
            <substitutions/>
          </text-style>
          <text-format placeDirectionSymbol="0" formatNumbers="0" useMaxLineLengthForAutoWrap="1" autoWrapLength="0" decimals="3" rightDirectionSymbol=">" plussign="0" addDirectionSymbol="0" wrapChar="" reverseDirectionSymbol="0" multilineAlign="0" leftDirectionSymbol="&lt;"/>
          <placement preserveRotation="1" repeatDistanceUnits="MM" placement="0" placementFlags="10" fitInPolygonOnly="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" rotationAngle="0" distMapUnitScale="3x:0,0,0,0,0,0" offsetType="0" yOffset="0" maxCurvedCharAngleOut="-25" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleIn="25" centroidWhole="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" priority="5" dist="0" centroidInside="0" distUnits="MapUnit" repeatDistance="0" quadOffset="4" offsetUnits="MapUnit" xOffset="0"/>
          <rendering obstacle="0" scaleMin="1" limitNumLabels="0" upsidedownLabels="0" fontLimitPixelSize="0" mergeLines="0" fontMaxPixelSize="10000" obstacleFactor="1" labelPerPart="0" drawLabels="1" minFeatureSize="0" maxNumLabels="50" fontMinPixelSize="3" zIndex="0" obstacleType="0" displayAll="1" scaleVisibility="1" scaleMax="2500"/>
          <dd_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="PositionX" type="Map">
                  <Option name="active" value="true" type="bool"/>
                  <Option name="expression" value="if ( &#xd;&#xa;&#xd;&#xa;&#x9;$x &lt; &quot;LABEL_X&quot;,&#xd;&#xa;&#x9;&#xd;&#xa;&#x9; &quot;LABEL_X&quot; + (0.017 * @map_scale),&#xd;&#xa;&#x9;&#xd;&#xa;&#x9; &quot;LABEL_X&quot; - (0.0185 * @map_scale)&#xd;&#xa;&#x9;&#xd;&#xa;&#x9;)" type="QString"/>
                  <Option name="type" value="3" type="int"/>
                </Option>
                <Option name="PositionY" type="Map">
                  <Option name="active" value="true" type="bool"/>
                  <Option name="expression" value="&quot;LABEL_Y&quot; + (0.0020 * @map_scale)" type="QString"/>
                  <Option name="type" value="3" type="int"/>
                </Option>
                <Option name="Show" type="Map">
                  <Option name="active" value="true" type="bool"/>
                  <Option name="field" value="LABEL_VIS" type="QString"/>
                  <Option name="type" value="2" type="int"/>
                </Option>
              </Option>
              <Option name="type" value="collection" type="QString"/>
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
    <property key="embeddedWidgets/count" value="0"/>
    <property key="labeling/addDirectionSymbol" value="false"/>
    <property key="labeling/angleOffset" value="0"/>
    <property key="labeling/blendMode" value="0"/>
    <property key="labeling/bufferBlendMode" value="0"/>
    <property key="labeling/bufferColorA" value="255"/>
    <property key="labeling/bufferColorB" value="255"/>
    <property key="labeling/bufferColorG" value="255"/>
    <property key="labeling/bufferColorR" value="255"/>
    <property key="labeling/bufferDraw" value="true"/>
    <property key="labeling/bufferJoinStyle" value="64"/>
    <property key="labeling/bufferNoFill" value="false"/>
    <property key="labeling/bufferSize" value="0.7"/>
    <property key="labeling/bufferSizeInMapUnits" value="false"/>
    <property key="labeling/bufferSizeMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/bufferTransp" value="0"/>
    <property key="labeling/centroidInside" value="false"/>
    <property key="labeling/centroidWhole" value="false"/>
    <property key="labeling/dataDefined/PositionX" value="1~~0~~~~LABEL_X"/>
    <property key="labeling/dataDefined/PositionY" value="1~~0~~~~LABEL_Y"/>
    <property key="labeling/dataDefined/Show" value="1~~0~~~~LABEL_VIS"/>
    <property key="labeling/decimals" value="3"/>
    <property key="labeling/displayAll" value="false"/>
    <property key="labeling/dist" value="5"/>
    <property key="labeling/distInMapUnits" value="true"/>
    <property key="labeling/distMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/drawLabels" value="true"/>
    <property key="labeling/enabled" value="true"/>
    <property key="labeling/fieldName" value="&#x9; &quot;Nodo_tipo&quot;    ||   '\n'  || &#xd;&#xa;&#x9;  'CT = '  || &quot;CT_(N)&quot;   ||  '\n'   ||  &#xd;&#xa;&#x9;   'CF = '  ||&quot;CF_nodo&quot;   ||   '\n'  || &#xd;&#xa;&#x9;   'h = '  ||&quot;h_nodo_NT&quot;   || 'm'"/>
    <property key="labeling/fitInPolygonOnly" value="false"/>
    <property key="labeling/fontCapitals" value="0"/>
    <property key="labeling/fontFamily" value="MS Shell Dlg 2"/>
    <property key="labeling/fontItalic" value="false"/>
    <property key="labeling/fontLetterSpacing" value="0"/>
    <property key="labeling/fontLimitPixelSize" value="false"/>
    <property key="labeling/fontMaxPixelSize" value="10000"/>
    <property key="labeling/fontMinPixelSize" value="3"/>
    <property key="labeling/fontSize" value="8"/>
    <property key="labeling/fontSizeInMapUnits" value="false"/>
    <property key="labeling/fontSizeMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/fontStrikeout" value="false"/>
    <property key="labeling/fontUnderline" value="false"/>
    <property key="labeling/fontWeight" value="50"/>
    <property key="labeling/fontWordSpacing" value="0"/>
    <property key="labeling/formatNumbers" value="false"/>
    <property key="labeling/isExpression" value="true"/>
    <property key="labeling/labelOffsetInMapUnits" value="true"/>
    <property key="labeling/labelOffsetMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/labelPerPart" value="false"/>
    <property key="labeling/leftDirectionSymbol" value="&lt;"/>
    <property key="labeling/limitNumLabels" value="false"/>
    <property key="labeling/maxCurvedCharAngleIn" value="20"/>
    <property key="labeling/maxCurvedCharAngleOut" value="-20"/>
    <property key="labeling/maxNumLabels" value="2000"/>
    <property key="labeling/mergeLines" value="false"/>
    <property key="labeling/minFeatureSize" value="0"/>
    <property key="labeling/multilineAlign" value="0"/>
    <property key="labeling/multilineHeight" value="1"/>
    <property key="labeling/namedStyle" value="Normal"/>
    <property key="labeling/obstacle" value="true"/>
    <property key="labeling/obstacleFactor" value="0.82"/>
    <property key="labeling/obstacleType" value="0"/>
    <property key="labeling/offsetType" value="0"/>
    <property key="labeling/placeDirectionSymbol" value="0"/>
    <property key="labeling/placement" value="0"/>
    <property key="labeling/placementFlags" value="10"/>
    <property key="labeling/plussign" value="false"/>
    <property key="labeling/predefinedPositionOrder" value="TR,TL,BR,BL,R,L,TSR,BSR"/>
    <property key="labeling/preserveRotation" value="true"/>
    <property key="labeling/previewBkgrdColor" value="#ffffff"/>
    <property key="labeling/priority" value="5"/>
    <property key="labeling/quadOffset" value="4"/>
    <property key="labeling/repeatDistance" value="0"/>
    <property key="labeling/repeatDistanceMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/repeatDistanceUnit" value="1"/>
    <property key="labeling/reverseDirectionSymbol" value="false"/>
    <property key="labeling/rightDirectionSymbol" value=">"/>
    <property key="labeling/scaleMax" value="6000"/>
    <property key="labeling/scaleMin" value="1"/>
    <property key="labeling/scaleVisibility" value="true"/>
    <property key="labeling/shadowBlendMode" value="6"/>
    <property key="labeling/shadowColorB" value="0"/>
    <property key="labeling/shadowColorG" value="0"/>
    <property key="labeling/shadowColorR" value="0"/>
    <property key="labeling/shadowDraw" value="false"/>
    <property key="labeling/shadowOffsetAngle" value="135"/>
    <property key="labeling/shadowOffsetDist" value="1"/>
    <property key="labeling/shadowOffsetGlobal" value="true"/>
    <property key="labeling/shadowOffsetMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shadowOffsetUnits" value="1"/>
    <property key="labeling/shadowRadius" value="1.5"/>
    <property key="labeling/shadowRadiusAlphaOnly" value="false"/>
    <property key="labeling/shadowRadiusMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shadowRadiusUnits" value="1"/>
    <property key="labeling/shadowScale" value="100"/>
    <property key="labeling/shadowTransparency" value="30"/>
    <property key="labeling/shadowUnder" value="0"/>
    <property key="labeling/shapeBlendMode" value="0"/>
    <property key="labeling/shapeBorderColorA" value="255"/>
    <property key="labeling/shapeBorderColorB" value="128"/>
    <property key="labeling/shapeBorderColorG" value="128"/>
    <property key="labeling/shapeBorderColorR" value="128"/>
    <property key="labeling/shapeBorderWidth" value="0"/>
    <property key="labeling/shapeBorderWidthMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shapeBorderWidthUnits" value="1"/>
    <property key="labeling/shapeDraw" value="false"/>
    <property key="labeling/shapeFillColorA" value="255"/>
    <property key="labeling/shapeFillColorB" value="255"/>
    <property key="labeling/shapeFillColorG" value="255"/>
    <property key="labeling/shapeFillColorR" value="255"/>
    <property key="labeling/shapeJoinStyle" value="64"/>
    <property key="labeling/shapeOffsetMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shapeOffsetUnits" value="1"/>
    <property key="labeling/shapeOffsetX" value="0"/>
    <property key="labeling/shapeOffsetY" value="0"/>
    <property key="labeling/shapeRadiiMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shapeRadiiUnits" value="1"/>
    <property key="labeling/shapeRadiiX" value="0"/>
    <property key="labeling/shapeRadiiY" value="0"/>
    <property key="labeling/shapeRotation" value="0"/>
    <property key="labeling/shapeRotationType" value="0"/>
    <property key="labeling/shapeSVGFile" value=""/>
    <property key="labeling/shapeSizeMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shapeSizeType" value="0"/>
    <property key="labeling/shapeSizeUnits" value="1"/>
    <property key="labeling/shapeSizeX" value="0"/>
    <property key="labeling/shapeSizeY" value="0"/>
    <property key="labeling/shapeTransparency" value="0"/>
    <property key="labeling/shapeType" value="0"/>
    <property key="labeling/substitutions" value="&lt;substitutions/>"/>
    <property key="labeling/textColorA" value="255"/>
    <property key="labeling/textColorB" value="0"/>
    <property key="labeling/textColorG" value="0"/>
    <property key="labeling/textColorR" value="170"/>
    <property key="labeling/textTransp" value="0"/>
    <property key="labeling/upsidedownLabels" value="0"/>
    <property key="labeling/useSubstitutions" value="false"/>
    <property key="labeling/wrapChar" value=""/>
    <property key="labeling/xOffset" value="0"/>
    <property key="labeling/yOffset" value="0"/>
    <property key="labeling/zIndex" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Pie">
    <DiagramCategory lineSizeScale="3x:0,0,0,0,0,0" labelPlacementMethod="XHeight" height="15" opacity="1" backgroundAlpha="255" minimumSize="0" lineSizeType="MM" barWidth="5" enabled="0" maxScaleDenominator="1e+08" backgroundColor="#ffffff" penColor="#000000" width="15" sizeType="MM" scaleDependency="Area" diagramOrientation="Up" penAlpha="255" scaleBasedVisibility="0" minScaleDenominator="100000" penWidth="0" rotationOffset="270" sizeScale="3x:0,0,0,0,0,0">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
      <attribute color="#000000" field="" label=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings zIndex="0" obstacle="0" placement="0" showAll="1" priority="0" dist="0" linePlacementFlags="2">
    <properties>
      <Option type="Map">
        <Option name="name" value="" type="QString"/>
        <Option name="properties" type="Map">
          <Option name="show" type="Map">
            <Option name="active" value="true" type="bool"/>
            <Option name="field" value="AUX05" type="QString"/>
            <Option name="type" value="2" type="int"/>
          </Option>
        </Option>
        <Option name="type" value="collection" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="CT_(N)">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" value="0" type="QString"/>
            <Option name="UseHtml" value="0" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="ID_UC">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" value="0" type="QString"/>
            <Option name="UseHtml" value="0" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX04">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" value="0" type="QString"/>
            <Option name="UseHtml" value="0" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX05">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" value="0" type="QString"/>
            <Option name="UseHtml" value="0" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX06">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" value="0" type="QString"/>
            <Option name="UseHtml" value="0" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="LABEL_X">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" value="0" type="QString"/>
            <Option name="UseHtml" value="0" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="LABEL_Y">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" value="0" type="QString"/>
            <Option name="UseHtml" value="0" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="LABEL_VIS">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" value="0" type="QString"/>
            <Option name="UseHtml" value="0" type="QString"/>
          </Option>
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
    <field name="Id_NODO_(n">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" value="0" type="QString"/>
            <Option name="UseHtml" value="0" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Nodo_tipo">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" value="0" type="QString"/>
            <Option name="UseHtml" value="0" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="CF_nodo">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" value="0" type="QString"/>
            <Option name="UseHtml" value="0" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="h_nodo_NT">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" value="0" type="QString"/>
            <Option name="UseHtml" value="0" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="h_nodo_tp">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" value="0" type="QString"/>
            <Option name="UseHtml" value="0" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="CItrd_nodo">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" value="0" type="QString"/>
            <Option name="UseHtml" value="0" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Tap_nodo">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" value="0" type="QString"/>
            <Option name="UseHtml" value="0" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" field="CT_(N)" index="0"/>
    <alias name="" field="ID_UC" index="1"/>
    <alias name="" field="AUX04" index="2"/>
    <alias name="" field="AUX05" index="3"/>
    <alias name="" field="AUX06" index="4"/>
    <alias name="" field="LABEL_X" index="5"/>
    <alias name="" field="LABEL_Y" index="6"/>
    <alias name="" field="LABEL_VIS" index="7"/>
    <alias name="" field="CF_NODO_2" index="8"/>
    <alias name="" field="H_NODO_TP2" index="9"/>
    <alias name="" field="Id_NODO_(n" index="10"/>
    <alias name="" field="Nodo_tipo" index="11"/>
    <alias name="" field="CF_nodo" index="12"/>
    <alias name="" field="h_nodo_NT" index="13"/>
    <alias name="" field="h_nodo_tp" index="14"/>
    <alias name="" field="CItrd_nodo" index="15"/>
    <alias name="" field="Tap_nodo" index="16"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" field="CT_(N)" applyOnUpdate="0"/>
    <default expression="" field="ID_UC" applyOnUpdate="0"/>
    <default expression="" field="AUX04" applyOnUpdate="0"/>
    <default expression="" field="AUX05" applyOnUpdate="0"/>
    <default expression="" field="AUX06" applyOnUpdate="0"/>
    <default expression="" field="LABEL_X" applyOnUpdate="0"/>
    <default expression="" field="LABEL_Y" applyOnUpdate="0"/>
    <default expression="" field="LABEL_VIS" applyOnUpdate="0"/>
    <default expression="" field="CF_NODO_2" applyOnUpdate="0"/>
    <default expression="" field="H_NODO_TP2" applyOnUpdate="0"/>
    <default expression="" field="Id_NODO_(n" applyOnUpdate="0"/>
    <default expression="" field="Nodo_tipo" applyOnUpdate="0"/>
    <default expression="" field="CF_nodo" applyOnUpdate="0"/>
    <default expression="" field="h_nodo_NT" applyOnUpdate="0"/>
    <default expression="" field="h_nodo_tp" applyOnUpdate="0"/>
    <default expression="" field="CItrd_nodo" applyOnUpdate="0"/>
    <default expression="" field="Tap_nodo" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint constraints="0" unique_strength="0" field="CT_(N)" notnull_strength="0" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" field="ID_UC" notnull_strength="0" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" field="AUX04" notnull_strength="0" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" field="AUX05" notnull_strength="0" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" field="AUX06" notnull_strength="0" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" field="LABEL_X" notnull_strength="0" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" field="LABEL_Y" notnull_strength="0" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" field="LABEL_VIS" notnull_strength="0" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" field="CF_NODO_2" notnull_strength="0" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" field="H_NODO_TP2" notnull_strength="0" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" field="Id_NODO_(n" notnull_strength="0" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" field="Nodo_tipo" notnull_strength="0" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" field="CF_nodo" notnull_strength="0" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" field="h_nodo_NT" notnull_strength="0" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" field="h_nodo_tp" notnull_strength="0" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" field="CItrd_nodo" notnull_strength="0" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" field="Tap_nodo" notnull_strength="0" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" field="CT_(N)" desc=""/>
    <constraint exp="" field="ID_UC" desc=""/>
    <constraint exp="" field="AUX04" desc=""/>
    <constraint exp="" field="AUX05" desc=""/>
    <constraint exp="" field="AUX06" desc=""/>
    <constraint exp="" field="LABEL_X" desc=""/>
    <constraint exp="" field="LABEL_Y" desc=""/>
    <constraint exp="" field="LABEL_VIS" desc=""/>
    <constraint exp="" field="CF_NODO_2" desc=""/>
    <constraint exp="" field="H_NODO_TP2" desc=""/>
    <constraint exp="" field="Id_NODO_(n" desc=""/>
    <constraint exp="" field="Nodo_tipo" desc=""/>
    <constraint exp="" field="CF_nodo" desc=""/>
    <constraint exp="" field="h_nodo_NT" desc=""/>
    <constraint exp="" field="h_nodo_tp" desc=""/>
    <constraint exp="" field="CItrd_nodo" desc=""/>
    <constraint exp="" field="Tap_nodo" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" actionWidgetStyle="dropDown" sortExpression="">
    <columns>
      <column name="AUX05" width="-1" hidden="0" type="field"/>
      <column name="AUX04" width="-1" hidden="0" type="field"/>
      <column name="AUX06" width="-1" hidden="0" type="field"/>
      <column name="LABEL_VIS" width="-1" hidden="0" type="field"/>
      <column name="CT_(N)" width="-1" hidden="0" type="field"/>
      <column name="LABEL_X" width="-1" hidden="0" type="field"/>
      <column name="LABEL_Y" width="-1" hidden="0" type="field"/>
      <column name="ID_UC" width="-1" hidden="0" type="field"/>
      <column name="Id_NODO_(n" width="-1" hidden="0" type="field"/>
      <column name="Nodo_tipo" width="-1" hidden="0" type="field"/>
      <column name="CF_nodo" width="-1" hidden="0" type="field"/>
      <column name="h_nodo_NT" width="-1" hidden="0" type="field"/>
      <column name="h_nodo_tp" width="-1" hidden="0" type="field"/>
      <column width="-1" hidden="1" type="actions"/>
      <column name="CItrd_nodo" width="-1" hidden="0" type="field"/>
      <column name="Tap_nodo" width="-1" hidden="0" type="field"/>
      <column name="CF_NODO_2" width="-1" hidden="0" type="field"/>
      <column name="H_NODO_TP2" width="-1" hidden="0" type="field"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1">.</editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath>.</editforminitfilepath>
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
  <mapTip>cat</mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
