<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyLocal="1" version="3.4.2-Madeira" maxScale="100000" minScale="1e+08" labelsEnabled="1" hasScaleBasedVisibilityFlag="0" styleCategories="AllStyleCategories" simplifyDrawingHints="0" simplifyAlgorithm="0" readOnly="0" simplifyDrawingTol="1" simplifyMaxScale="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 type="singleSymbol" enableorderby="0" forceraster="0" symbollevels="0">
    <symbols>
      <symbol alpha="1" type="marker" name="0" clip_to_extent="1">
        <layer class="GeometryGenerator" enabled="1" pass="0" locked="0">
          <prop k="SymbolType" v="Line"/>
          <prop k="geometryModifier" v="CASE &#xd;&#xa;WHEN @map_scale  &lt; 2001&#xd;&#xa;THEN  &#xd;&#xa;&#xd;&#xa;If ($x &lt; &quot;LABEL_X&quot;,&#xd;&#xa;&#xd;&#xa;make_line (&#xd;&#xa;make_point( &quot;LABEL_X&quot; +22 , &quot;LABEL_Y&quot; + 5 ),&#xd;&#xa;make_point( &quot;LABEL_X&quot; , &quot;LABEL_Y&quot; + 5 ),&#xd;&#xa;make_point( x(centroid( $geometry )), y(centroid( $geometry )))&#xd;&#xa; ),&#xd;&#xa; &#xd;&#xa;make_line (&#xd;&#xa;make_point( &quot;LABEL_X&quot; -1 , &quot;LABEL_Y&quot; + 5 ),&#xd;&#xa;make_point( &quot;LABEL_X&quot; + 22 , &quot;LABEL_Y&quot; + 5 ),&#xd;&#xa;make_point( x(centroid( $geometry )), y(centroid( $geometry )))&#xd;&#xa; )&#xd;&#xa; &#xd;&#xa; )&#xd;&#xa; &#xd;&#xa; END"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="1" type="line" name="@0@0" clip_to_extent="1">
            <layer class="SimpleLine" enabled="1" pass="0" locked="0">
              <prop k="capstyle" v="square"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="customdash_unit" v="MM"/>
              <prop k="draw_inside_polygon" v="0"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="line_color" v="0,0,0,255"/>
              <prop k="line_style" v="solid"/>
              <prop k="line_width" v="0.25"/>
              <prop k="line_width_unit" v="MapUnit"/>
              <prop k="offset" v="0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="use_custom_dash" v="0"/>
              <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option name="properties"/>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer class="SimpleMarker" enabled="1" pass="0" locked="0">
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
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <labeling type="rule-based">
    <rules key="{c2f0cab1-047e-46b6-b667-070d8586abc3}">
      <rule key="{e3b84e4d-c22c-40d5-9ef1-142951eb56be}">
        <settings>
          <text-style fontSize="3.6" blendMode="0" fontWeight="50" fontSizeMapUnitScale="3x:0,0,0,0,0,0" textOpacity="1" fontLetterSpacing="0" multilineHeight="1.15" fontStrikeout="0" isExpression="1" fieldName=" &#x9;  'CT  '  ||&quot;CT_(N)&quot;  ||  '\n'   ||  &#xd;&#xa;&#x9;   'CF  '  ||&quot;CF_nodo&quot;&#xd;&#xa;" fontWordSpacing="0" useSubstitutions="0" fontItalic="0" namedStyle="Normal" fontCapitals="0" previewBkgrdColor="#ffffff" textColor="0,0,0,255" fontUnderline="0" fontSizeUnit="MapUnit" fontFamily="Arial">
            <text-buffer bufferColor="255,255,255,255" bufferDraw="1" bufferOpacity="1" bufferNoFill="0" bufferSizeUnits="MapUnit" bufferSize="0.5" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferBlendMode="0" bufferJoinStyle="128"/>
            <background shapeBorderColor="128,128,128,255" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthUnit="MM" shapeSizeX="0" shapeBorderWidth="0" shapeJoinStyle="64" shapeBlendMode="0" shapeOffsetUnit="MM" shapeRotationType="0" shapeDraw="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiY="0" shapeOpacity="1" shapeFillColor="255,255,255,255" shapeOffsetX="0" shapeRadiiX="0" shapeRadiiUnit="MM" shapeType="0" shapeRotation="0" shapeSizeType="0" shapeSVGFile="" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetY="0" shapeSizeUnit="MM" shapeSizeY="0"/>
            <shadow shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOpacity="0.7" shadowRadiusUnit="MM" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetAngle="135" shadowOffsetUnit="MM" shadowBlendMode="6" shadowDraw="0" shadowOffsetGlobal="1" shadowColor="0,0,0,255" shadowScale="100" shadowUnder="0" shadowOffsetDist="1" shadowRadius="1.5" shadowRadiusAlphaOnly="0"/>
            <substitutions/>
          </text-style>
          <text-format autoWrapLength="0" useMaxLineLengthForAutoWrap="1" decimals="3" addDirectionSymbol="0" rightDirectionSymbol=">" wrapChar="" multilineAlign="0" formatNumbers="0" plussign="0" reverseDirectionSymbol="0" leftDirectionSymbol="&lt;" placeDirectionSymbol="0"/>
          <placement repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" distMapUnitScale="3x:0,0,0,0,0,0" fitInPolygonOnly="0" repeatDistanceUnits="MM" placementFlags="10" yOffset="0" distUnits="MM" offsetType="0" priority="5" maxCurvedCharAngleIn="25" dist="0" offsetUnits="MapUnit" centroidWhole="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" rotationAngle="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" placement="0" quadOffset="4" centroidInside="0" preserveRotation="1" repeatDistance="0" maxCurvedCharAngleOut="-25" xOffset="0"/>
          <rendering mergeLines="0" zIndex="0" obstacleFactor="1" displayAll="1" drawLabels="1" fontMinPixelSize="3" scaleMax="2001" upsidedownLabels="0" maxNumLabels="2000" obstacle="0" scaleMin="1" scaleVisibility="1" fontLimitPixelSize="0" minFeatureSize="0" labelPerPart="0" fontMaxPixelSize="10000" limitNumLabels="0" obstacleType="0"/>
          <dd_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option type="Map" name="properties">
                <Option type="Map" name="PositionX">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="field" value="LABEL_X"/>
                  <Option type="int" name="type" value="2"/>
                </Option>
                <Option type="Map" name="PositionY">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="field" value="LABEL_Y"/>
                  <Option type="int" name="type" value="2"/>
                </Option>
              </Option>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </dd_properties>
        </settings>
      </rule>
      <rule key="{a6294ea9-c86b-4480-9d43-9c2869bd939a}">
        <settings>
          <text-style fontSize="3.6" blendMode="0" fontWeight="50" fontSizeMapUnitScale="3x:0,0,0,0,0,0" textOpacity="1" fontLetterSpacing="0" multilineHeight="1" fontStrikeout="0" isExpression="1" fieldName="If (&#xd;&#xa;&#xd;&#xa;&#x9;$x &lt; &quot;LABEL_X&quot;, &#xd;&#xa;&#x9;&#xd;&#xa;&#x9;&quot;h_nodo_NT&quot;  ||'  '||  &quot;Nodo_tipo&quot;,&#xd;&#xa;&#xd;&#xa;&#x9; &quot;Nodo_tipo&quot; ||'  '||&quot;h_nodo_NT&quot; &#xd;&#xa;&#x9;&#xd;&#xa;&#x9;)" fontWordSpacing="-1.5" useSubstitutions="0" fontItalic="0" namedStyle="Normal" fontCapitals="0" previewBkgrdColor="#ffffff" textColor="0,0,0,255" fontUnderline="0" fontSizeUnit="MapUnit" fontFamily="Arial">
            <text-buffer bufferColor="255,255,255,255" bufferDraw="1" bufferOpacity="1" bufferNoFill="0" bufferSizeUnits="MapUnit" bufferSize="0.5000000000000001" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferBlendMode="0" bufferJoinStyle="128"/>
            <background shapeBorderColor="128,128,128,255" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthUnit="MM" shapeSizeX="0" shapeBorderWidth="0" shapeJoinStyle="64" shapeBlendMode="0" shapeOffsetUnit="MM" shapeRotationType="0" shapeDraw="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiY="0" shapeOpacity="1" shapeFillColor="255,255,255,255" shapeOffsetX="0" shapeRadiiX="0" shapeRadiiUnit="MM" shapeType="0" shapeRotation="0" shapeSizeType="0" shapeSVGFile="" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetY="0" shapeSizeUnit="MM" shapeSizeY="0"/>
            <shadow shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOpacity="0.7" shadowRadiusUnit="MM" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetAngle="135" shadowOffsetUnit="MM" shadowBlendMode="6" shadowDraw="0" shadowOffsetGlobal="1" shadowColor="0,0,0,255" shadowScale="100" shadowUnder="0" shadowOffsetDist="1" shadowRadius="1.5" shadowRadiusAlphaOnly="0"/>
            <substitutions/>
          </text-style>
          <text-format autoWrapLength="0" useMaxLineLengthForAutoWrap="1" decimals="3" addDirectionSymbol="0" rightDirectionSymbol=">" wrapChar="" multilineAlign="0" formatNumbers="0" plussign="0" reverseDirectionSymbol="0" leftDirectionSymbol="&lt;" placeDirectionSymbol="0"/>
          <placement repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" distMapUnitScale="3x:0,0,0,0,0,0" fitInPolygonOnly="0" repeatDistanceUnits="MM" placementFlags="10" yOffset="0" distUnits="MapUnit" offsetType="0" priority="5" maxCurvedCharAngleIn="25" dist="0" offsetUnits="MapUnit" centroidWhole="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" rotationAngle="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" placement="0" quadOffset="4" centroidInside="0" preserveRotation="1" repeatDistance="0" maxCurvedCharAngleOut="-25" xOffset="0"/>
          <rendering mergeLines="0" zIndex="0" obstacleFactor="1" displayAll="1" drawLabels="1" fontMinPixelSize="3" scaleMax="2001" upsidedownLabels="0" maxNumLabels="2000" obstacle="0" scaleMin="1" scaleVisibility="1" fontLimitPixelSize="0" minFeatureSize="0" labelPerPart="0" fontMaxPixelSize="10000" limitNumLabels="0" obstacleType="0"/>
          <dd_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option type="Map" name="properties">
                <Option type="Map" name="PositionX">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="if ( &#xd;&#xa;&#xd;&#xa;&#x9;$x &lt; &quot;LABEL_X&quot;,&#xd;&#xa;&#x9;&#xd;&#xa;&#x9; &quot;LABEL_X&quot; + 23  ,&#xd;&#xa;&#x9;&#xd;&#xa;&#x9; &quot;LABEL_X&quot; - 23 &#xd;&#xa;&#x9;&#xd;&#xa;&#x9;)"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
                <Option type="Map" name="PositionY">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="&quot;LABEL_Y&quot; + 3"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
              </Option>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </dd_properties>
        </settings>
      </rule>
    </rules>
  </labeling>
  <customproperties>
    <property key="dualview/previewExpressions" value="ID_UC"/>
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
    <DiagramCategory penWidth="0" backgroundColor="#ffffff" minimumSize="0" lineSizeScale="3x:0,0,0,0,0,0" height="15" opacity="1" backgroundAlpha="255" penAlpha="255" width="15" sizeScale="3x:0,0,0,0,0,0" diagramOrientation="Up" scaleBasedVisibility="0" minScaleDenominator="100000" sizeType="MM" maxScaleDenominator="1e+08" penColor="#000000" scaleDependency="Area" barWidth="5" rotationOffset="270" enabled="0" labelPlacementMethod="XHeight" lineSizeType="MM">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
      <attribute color="#000000" label="" field=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings showAll="1" zIndex="0" placement="0" linePlacementFlags="2" dist="0" priority="0" obstacle="0">
    <properties>
      <Option type="Map">
        <Option type="QString" name="name" value=""/>
        <Option type="Map" name="properties">
          <Option type="Map" name="show">
            <Option type="bool" name="active" value="true"/>
            <Option type="QString" name="field" value="AUX05"/>
            <Option type="int" name="type" value="2"/>
          </Option>
        </Option>
        <Option type="QString" name="type" value="collection"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="AUX05">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX04">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX06">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="LABEL_VIS">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="CT_(N)">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="LABEL_X">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="LABEL_Y">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="ID_UC">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Id_NODO_(n">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Nodo_tipo">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="CF_nodo">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="h_nodo_NT">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="h_nodo_tp">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="CItrd_nodo">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Tap_nodo">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" field="AUX05" index="0"/>
    <alias name="" field="AUX04" index="1"/>
    <alias name="" field="AUX06" index="2"/>
    <alias name="" field="LABEL_VIS" index="3"/>
    <alias name="" field="CT_(N)" index="4"/>
    <alias name="" field="LABEL_X" index="5"/>
    <alias name="" field="LABEL_Y" index="6"/>
    <alias name="" field="ID_UC" index="7"/>
    <alias name="" field="Id_NODO_(n" index="8"/>
    <alias name="" field="Nodo_tipo" index="9"/>
    <alias name="" field="CF_nodo" index="10"/>
    <alias name="" field="h_nodo_NT" index="11"/>
    <alias name="" field="h_nodo_tp" index="12"/>
    <alias name="" field="CItrd_nodo" index="13"/>
    <alias name="" field="Tap_nodo" index="14"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default applyOnUpdate="0" expression="" field="AUX05"/>
    <default applyOnUpdate="0" expression="" field="AUX04"/>
    <default applyOnUpdate="0" expression="" field="AUX06"/>
    <default applyOnUpdate="0" expression="" field="LABEL_VIS"/>
    <default applyOnUpdate="0" expression="" field="CT_(N)"/>
    <default applyOnUpdate="0" expression="" field="LABEL_X"/>
    <default applyOnUpdate="0" expression="" field="LABEL_Y"/>
    <default applyOnUpdate="0" expression="" field="ID_UC"/>
    <default applyOnUpdate="0" expression="" field="Id_NODO_(n"/>
    <default applyOnUpdate="0" expression="" field="Nodo_tipo"/>
    <default applyOnUpdate="0" expression="" field="CF_nodo"/>
    <default applyOnUpdate="0" expression="" field="h_nodo_NT"/>
    <default applyOnUpdate="0" expression="" field="h_nodo_tp"/>
    <default applyOnUpdate="0" expression="" field="CItrd_nodo"/>
    <default applyOnUpdate="0" expression="" field="Tap_nodo"/>
  </defaults>
  <constraints>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" field="AUX05" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" field="AUX04" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" field="AUX06" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" field="LABEL_VIS" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" field="CT_(N)" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" field="LABEL_X" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" field="LABEL_Y" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" field="ID_UC" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" field="Id_NODO_(n" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" field="Nodo_tipo" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" field="CF_nodo" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" field="h_nodo_NT" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" field="h_nodo_tp" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" field="CItrd_nodo" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" field="Tap_nodo" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" field="AUX05" desc=""/>
    <constraint exp="" field="AUX04" desc=""/>
    <constraint exp="" field="AUX06" desc=""/>
    <constraint exp="" field="LABEL_VIS" desc=""/>
    <constraint exp="" field="CT_(N)" desc=""/>
    <constraint exp="" field="LABEL_X" desc=""/>
    <constraint exp="" field="LABEL_Y" desc=""/>
    <constraint exp="" field="ID_UC" desc=""/>
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
  <attributetableconfig sortOrder="0" sortExpression="" actionWidgetStyle="dropDown">
    <columns>
      <column hidden="0" width="-1" type="field" name="AUX05"/>
      <column hidden="0" width="-1" type="field" name="AUX04"/>
      <column hidden="0" width="-1" type="field" name="AUX06"/>
      <column hidden="0" width="-1" type="field" name="LABEL_VIS"/>
      <column hidden="0" width="-1" type="field" name="CT_(N)"/>
      <column hidden="0" width="-1" type="field" name="LABEL_X"/>
      <column hidden="0" width="-1" type="field" name="LABEL_Y"/>
      <column hidden="0" width="-1" type="field" name="ID_UC"/>
      <column hidden="0" width="-1" type="field" name="Id_NODO_(n"/>
      <column hidden="0" width="-1" type="field" name="Nodo_tipo"/>
      <column hidden="0" width="-1" type="field" name="CF_nodo"/>
      <column hidden="0" width="-1" type="field" name="h_nodo_NT"/>
      <column hidden="0" width="-1" type="field" name="h_nodo_tp"/>
      <column hidden="1" width="-1" type="actions"/>
      <column hidden="0" width="-1" type="field" name="CItrd_nodo"/>
      <column hidden="0" width="-1" type="field" name="Tap_nodo"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1">D:/PROGRA~1/QGIS3~1.4/bin</editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath>D:/PROGRA~1/QGIS3~1.4/bin</editforminitfilepath>
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
    <field name="CF_nodo" editable="1"/>
    <field name="CItrd_nodo" editable="1"/>
    <field name="CT_(N)" editable="1"/>
    <field name="ID_UC" editable="1"/>
    <field name="Id_NODO_(n" editable="1"/>
    <field name="LABEL_VIS" editable="1"/>
    <field name="LABEL_X" editable="1"/>
    <field name="LABEL_Y" editable="1"/>
    <field name="Nodo_tipo" editable="1"/>
    <field name="Tap_nodo" editable="1"/>
    <field name="fid" editable="1"/>
    <field name="h_nodo_NT" editable="1"/>
    <field name="h_nodo_tp" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="AUX04" labelOnTop="0"/>
    <field name="AUX05" labelOnTop="0"/>
    <field name="AUX06" labelOnTop="0"/>
    <field name="CF_nodo" labelOnTop="0"/>
    <field name="CItrd_nodo" labelOnTop="0"/>
    <field name="CT_(N)" labelOnTop="0"/>
    <field name="ID_UC" labelOnTop="0"/>
    <field name="Id_NODO_(n" labelOnTop="0"/>
    <field name="LABEL_VIS" labelOnTop="0"/>
    <field name="LABEL_X" labelOnTop="0"/>
    <field name="LABEL_Y" labelOnTop="0"/>
    <field name="Nodo_tipo" labelOnTop="0"/>
    <field name="Tap_nodo" labelOnTop="0"/>
    <field name="fid" labelOnTop="0"/>
    <field name="h_nodo_NT" labelOnTop="0"/>
    <field name="h_nodo_tp" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>ID_UC</previewExpression>
  <mapTip>cat</mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
