# Sequence

* `SELECT * FROM SYS.Sequences`
* `SELECT (NEXT VALUE FOR OSS_OWNER.TBL_CONTROL_CONDITIONS_SEQ) AS SequenceValue`
* Reset value

```sql
ALTER SEQUENCE OSS_OWNER.TBL_OUTPUT_AGREEMENT_SEQ
RESTART WITH 7012912 ;
GO
```
## References

* https://thorben-janssen.com/hibernate-tips-use-custom-sequence/
* https://vladmihalcea.com/jpa-entity-identifier-sequence/
* https://sqlhints.com/tag/getting-next-sequence-value-in-a-select-statement/
