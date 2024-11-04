
# google.generativeai.protos.UpdateDocumentRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/retriever_service.py#L339-L359">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request to update a ``Document``.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>

`document`<a id="document"></a>

</td>
<td>

`google.ai.generativelanguage.Document`

Required. The ``Document`` to update.

</td>
</tr><tr>
<td>

`update_mask`<a id="update_mask"></a>

</td>
<td>

`google.protobuf.field_mask_pb2.FieldMask`

Required. The list of fields to update. Currently, this only
supports updating ``display_name`` and ``custom_metadata``.

</td>
</tr>
</table>


