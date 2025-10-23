## Manual testing: Productivity Masters: backend (drf_api)

<table>
<tr>
<th style="color: gold">Action</th>
<th style="color: gold">Expected behaviour</th>
<th style="color: gold">Pass/Fail</th>
<tr>
<tr>
<td><strong style="color: gold">Click on link: [add link]</strong></td>
<td>The user is forwarded to the root route of the api; a JSON object can be seen with the message "Welcome to the Productivity Masters drf api!"</td>
<td>Pass</td>
</tr>
<tr>
<td><strong style="color: gold">NOT LOGGED IN</strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Add "/profiles" to the root route url</td>
<td>The user is forwarded to the Profile List view, where a list of all the users can be seen. The key "is_owner" on all of the respective JSON-objects is set to "false"</td>
<td>Pass</td>
</tr>
<tr>
<td>Add "/tasks" to the root route urls</td>
<td>The user is forwarded to the Task List view. As the user is not logged in, they are presented with the message "Authentication credentials were not provided."</td>
<td>Pass</td>
</tr>
<tr>
<td>Add "/categories" to the root route urls</td>
<td>The user is forwarded to the Category List view. As the user is not logged in, they are presented with the message "Authentication credentials were not provided."</td>
<td>Pass</td>
</tr>
<tr>
<td>Add "/reminders" to the root route urls</td>
<td>The user is forwarded to the Reminder List view. As the user is not logged in, they are presented with the message "Authentication credentials were not provided."</td>
<td>Pass</td>
</tr>
<td>Add "/attachments" to the root route urls</td>
<td>The user is forwarded to the Attachment List view. As the user is not logged in, they are presented with the message "Authentication credentials were not provided."</td>
<td>Pass</td>
</tr>
<tr>
<td><strong style="color: gold">LOGGED IN AS OSKAR</strong></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>Add "/profiles" to the root route url</td>
<td>The user is forwarded to the Profile List view, where a list of all the users can be seen. The key "is_owner" on the JSON-object for the user "Oskar" is set to "true". In all the others, it is set to "false"</td>
<td>Pass</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</table>


## Manual testing: Productivity Masters (frontend)

<table>
<tr>
<th style="color: gold">Action</th>
<th style="color: gold">Expected behaviour</th>
<th style="color: gold">Pass/Fail</th>
<tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong style="color: gold"></strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong style="color: gold"></strong></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</table>