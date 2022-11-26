{{ name | escape | underline}}

Qualified name: ``{{ fullname | escape }}``

.. currentmodule:: {{ module }}

.. autoclass:: {{ name }}
   :show-inheritance:
   :members:

   {% block methods %}
   {%- if methods %}
   .. rubric:: {{ _('Methods') }}

   .. autosummary::
      :nosignatures:
      {% for item in methods if item != '__init__' and item not in inherited_members %}
      ~{{ name }}.{{ item }}
      {%- endfor %}
   {%- endif %}
   {%- endblock %}

   {% block attributes %}
   {%- if attributes %}
   .. rubric:: {{ _('Inherited Attributes') }}

   .. autosummary::
     {% for item in attributes if item in inherited_members %}
     ~{{ name }}.{{ item }}
     {%- endfor %}
   {%- endif %}
   {% endblock %}