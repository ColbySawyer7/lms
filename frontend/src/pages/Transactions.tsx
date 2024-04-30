import {
  Create,
  Datagrid,
  Edit,
  EditButton,
  List,
  SimpleForm,
  TextField,
  TextInput,
  ReferenceField,
} from "react-admin";

export const TransactionList = (props: any) => (
  <List {...props} filters={[]}>
    <Datagrid>
      <TextField source="id" />
      <ReferenceField label="Book" source="book_id" reference="books">
        <TextField source="title" />
      </ReferenceField>
      <ReferenceField label="User" source="user_id" reference="users">
        <TextField source="email" />
      </ReferenceField>
      <ReferenceField label="Library" source="library_id" reference="libraries">
        <TextField source="name" />
      </ReferenceField>
      <EditButton />
    </Datagrid>
  </List>
);

export const TransactionEdit = (props: any) => (
  <Edit {...props}>
    <SimpleForm>
      <TextInput source="book_id" />
    </SimpleForm>
  </Edit>
);

export const TransactionCreate = (props: any) => (
  <Create {...props}>
    <SimpleForm>
      <TextInput source="book_id" />
    </SimpleForm>
  </Create>
);
